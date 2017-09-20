
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^products/', include('products.urls_api', namespace='products')),
    url(r'^carts/', include('carts.urls_api', namespace='carts')),
    url(r'^accounts/', include('accounts.urls_api', namespace='accounts')),
]
