from django.conf.urls import url

from . import views_api


urlpatterns = [   
     url(r'^cart-update/$', views_api.CartView.as_view(),name='cart-update'),

    ]