from rest_framework import generics,mixins
from .models import Product,Category,ProductFeatured,Variation

from rest_framework import permissions
from .serializers import ProductDetailSerializer,CategoryDetailSerializer,FeaturedDetailSerializer,VariationDetailSerializer

from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from itertools import chain
from accounts.models import User
# from .paginations import LargeResultsSetPagination
import datetime
# from interaction.models import AddImageVideo
from rest_framework.response import Response

class ProductDetailView(generics.RetrieveAPIView):
	authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
	permission_classes = [permissions.AllowAny,]
	serializer_class = VariationDetailSerializer
	queryset = Variation.objects.all()
	lookup_field = 'id'


# class ProjectListView(generics.ListAPIView):
# 	authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
# 	permission_classes = [permissions.AllowAny,]
# 	serializer_class = ProductDetailSerializer
# 	queryset = Product.objects.active()
# 	# pagination_class = LargeResultsSetPagination








class ProductFilterListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = ProductDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        type_filter = self.request.query_params.get('category',None)
        obj_id = self.request.query_params.get('obj_id',None)
        if type_filter == None: 
        	queryset = Product.objects.all().order_by('-id')
        	return queryset
        if type_filter == 'category':
            obj = get_object_or_404(Category,id=obj_id)
            queryset = Product.objects.filter(category=obj).order_by('-id')
        else:
            queryset = []
        return queryset



# class ProductNewListView(generics.ListAPIView):
#     authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
#     permission_classes = [permissions.AllowAny,]
#     serializer_class = ProductDetailSerializer
#     # pagination_class = LargeResultsSetPagination


#     def get_queryset(self):
#         count = self.request.query_params.get('count',None)
#         if count == None or count=='': 
#             queryset = Product.objects.all().order_by('-id')[:3]
#             return queryset
#         queryset = Product.objects.all().order_by('-id')[:int(count)]
#         return queryset

# class ProductRandomListView(generics.ListAPIView):
#     authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
#     permission_classes = [permissions.AllowAny,]
#     serializer_class = ProductDetailSerializer
#     # pagination_class = LargeResultsSetPagination


#     def get_queryset(self):
#         count = self.request.query_params.get('count',None)
#         if count == None or count=='': 
#             queryset = Product.objects.all().order_by('?')[:3]
#             return queryset
#         queryset = Product.objects.all().order_by('?')[:int(count)]
#         return queryset

class ProductCategoryListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = VariationDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        print("insnsnsnsns",id)
        if id != None or id!='': 

            queryset = Variation.objects.filter(product__categories__id=int(id))
            print("query",queryset)
            return queryset
        return []
	

class CategoryRandomListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = CategoryDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        count = self.request.query_params.get('count',None)
        if count == None or count=='': 
            queryset = Category.objects.all().order_by('?')[:3]
            return queryset
        queryset = Category.objects.all().order_by('-id')
        return queryset

class CategoryListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = CategoryDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        count = self.request.query_params.get('count',None)
        if count == None or count=='': 
            queryset = Category.objects.all()[:5]
            return queryset
        queryset = Category.objects.all().order_by('-id')
        return queryset

class FeaturedRandomListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = FeaturedDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        count = self.request.query_params.get('count',None)
        if count == None or count=='': 
            queryset = ProductFeatured.objects.all().order_by('?')[:3]
            return queryset
        queryset = ProductFeatured.objects.all().order_by('?')[:int(count)]
        return queryset


class ProductNewListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = VariationDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        count = self.request.query_params.get('count',None)
        if count == None or count=='': 
            queryset = Variation.objects.all().order_by('-id')[:3]
            return queryset
        queryset = Variation.objects.all().order_by('-id')[:int(count)]
        return queryset

class ProductRandomListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,JSONWebTokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    serializer_class = VariationDetailSerializer
    # pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        count = self.request.query_params.get('count',None)
        if count == None or count=='': 
            queryset = Variation.objects.all().order_by('?')[:3]
            return queryset
        queryset = Variation.objects.all().order_by('?')[:int(count)]
        return queryset