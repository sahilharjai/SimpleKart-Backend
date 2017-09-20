from rest_framework import generics,mixins
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.edit import FormMixin
from rest_framework.views import APIView
from rest_framework.response import Response


from products.models import Variation


from .models import Cart, CartItem
from .serializers import CartDetailSerializer,UserCartSerializer
from django.core.exceptions import ObjectDoesNotExist 


class CartView(APIView):
    def get(self, request):
        cart_id = self.request.query_params.get("cart_id",None)
        if cart_id == None or cart_id=="-1":
            print("in cart guest")
            cart = Cart()
            cart.tax_percentage = 0.075
            cart.save()
            cart_id = cart.id
        cart = Cart.objects.get(id=int(cart_id))
        # if request.user.is_authenticated():
        #     cart.user = request.user
        #     cart.save()
        item_id = request.query_params.get("item",None)
        delete_item = request.query_params.get("delete", False)
        flash_message = ""
        item_added = False
        if item_id:
            item_instance = get_object_or_404(Variation, id=item_id)
            qty = request.query_params.get("qty", 1)
            try:
                if int(qty) < 1:
                    delete_item = True
            except:
                raise Http404
            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item_instance)
            if created:
                flash_message = "Successfully added to the cart"
                item_added = True
            if delete_item==None or delete_item=='true' or delete_item==True:
                flash_message = "Item removed successfully."
                cart_item.delete()
            else:
                if not created:
                    flash_message = "Quantity has been updated successfully."
                cart_item.quantity = qty
                cart_item.save()
            try:
                total = cart_item.line_item_total
            except:
                total = None
            try:
                subtotal = cart_item.cart.subtotal
            except:
                subtotal = None

            try:
                cart_total = cart_item.cart.total
            except:
                cart_total = None

            try:
                tax_total = cart_item.cart.tax_total
            except:
                tax_total = None

            try:
                total_items = cart_item.cart.items.count()
            except:
                total_items = 0

            data = {
                    "deleted": delete_item, 
                    "item_added": item_added,
                    "line_total": total,
                    "subtotal": subtotal,
                    "cart_total": cart_total,
                    "tax_total": tax_total,
                    "flash_message": flash_message,
                    "total_items": total_items,
                    "cart_id":cart_id,
                    }
            return Response(data)
        try:
            cart_item = CartItem.objects.filter(cart=cart)
        except ObjectDoesNotExist:
            cart_item=None

        serializer= UserCartSerializer(cart_item,many=True,context={'request':request})
        return Response(serializer.data)

class ItemCountView(APIView):
    def get(self, request):
            cart_id = self.request.session.get("cart_id")
            if cart_id == None:
                count = 0
            else:
                cart = Cart.objects.get(id=cart_id)
                count = cart.items.count()
            return Response({"count": count})














