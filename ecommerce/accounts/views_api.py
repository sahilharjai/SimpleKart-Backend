from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status,permissions,mixins,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
import datetime
from datetime import datetime

from django.contrib.contenttypes.models import ContentType

import csv
from django.http import HttpResponse

from itertools import chain


from rest_framework_jwt.settings import api_settings
import datetime, random
from random import randint
from carts.models import Cart,CartItem
from .models import User,UserAddress,Order
from .serializers import UserRegistrationSerializer,UserAddressSerializer,UserDetailSerializer,UserOrderSerializer
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER





class Register(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print("request",request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(mobile=serializer.data['mobile'])[0]
            time = datetime.datetime.now()
            i=0
            string = ''
            while i<5:
                number = randint(0,9)
                number = str(number)
                string = string + number
                i=i+1
            # user.username = str(user.mobile)[-5:]+str(str(time).split(".")[0])[-5:]
            user.username = str(user.mobile)[-5:]+string
            user.save()
            new_user = authenticate(email=user.email,password=user.password)
            cart = Cart.objects.create(user=user)
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReturnRegisterStepOfUser(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]        
    def get(self,request):
        user = request.user
        if user.registration_complete:
            step = 6
            status = "complete"
        else:
            step =user.registration_stage
            status = "incomplete"
        message = {'status':status,'registration_step':step}
        return Response(message)


class UserDetailAddressView(APIView):
    def get(self,request,id):
        user = get_object_or_404(User,id=id)
        serializer = UserDetailSerializer(user,many=False,read_only=True)
        return Response(serializer.data)




class CheckUserExistsOrNot(APIView):
    permission_classes = [permissions.AllowAny]        
    def get(self,request,mobile):
        try:
            user = User.objects.get(mobile=mobile)
        except ObjectDoesNotExist:
            return Response({'status': 'User doesnt Exists'})
        if user!=request.user:
            return Response({'status':'User Already Registered'})
        else:
           return Response({'status': 'User doesnt Exists'}) 

class CreateUserAddressview(APIView):
    def get(self,request,id):
        if id==None or id=='':
            return None
        user = get_object_or_404(User,id=id)
        user_address = UserAddress.objects.filter(user=user)
        if user_address:
            serializer = UserAddressSerializer(user_address,many=True,read_only=True)
            return serializer.data
        return None


    def post(self,request,id):
        if id==None or id=='':
            return None
        user = get_object_or_404(User,id=id)
        user_address = UserAddress.objects.filter(user=user)
        if user_address.count() !=0:
            serializer = UserAddressSerializer(user_address[0],data=request.data)
            if serializer.is_valid():
                address = serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        address = UserAddressSerializer(data=request.data)
        if address.is_valid():
            add = address.save()
            add.user=request.user
            add.save()
            serializer = UserAddressSerializer(add,many=False,read_only=True)
            return Response(serializer.data)
        else:
            return Response(address.errors)


class CreateUserOrderview(APIView):

    def post(self,request,id):
        if id==None or id=='':
            return None
        user = get_object_or_404(User,id=id)
        user_cart = get_object_or_404(Cart,user=user)
        user_address = UserAddress.objects.filter(user=user)
        if user_cart and user_address:
            order_id=randint(10000,99999)
            order = Order(user=user,cart=user_cart,shipping_address=user_address[0],order_id=order_id)
            order.save()
            return Response("success")
        return Response("failure")



class RetriveUserOrderview(APIView):
    def get(self,request,id):
        print("ahahahahahahahahahahaha",id)
        if id==None or id=='':
            return None
        user = get_object_or_404(User,id=id)
        user_order = Order.objects.filter(user=user).order_by('-id')
        if user_order.count()!=0:
            order=user_order[0]
            serializer = UserOrderSerializer(order,many=False,read_only=True,context={'request':request})
            return Response(serializer.data)
        return None