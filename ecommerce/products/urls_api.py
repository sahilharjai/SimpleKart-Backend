from django.conf.urls import url

from . import views_api


urlpatterns = [   
    url(r'^product-detail/(?P<id>\d+)/$', views_api.ProductDetailView.as_view(),name='product-detail'),
    url(r'^product-filter-list/$', views_api.ProductFilterListView.as_view(),name='product-filter-list'),
    url(r'^product-new-list/$', views_api.ProductNewListView.as_view(),name='product-new-list'),
    url(r'^product-random-list/$', views_api.ProductRandomListView.as_view(),name='product-random-list'),
    url(r'^category-random-list/$', views_api.CategoryRandomListView.as_view(),name='category-random-list'),
    url(r'^featured-random-list/$', views_api.FeaturedRandomListView.as_view(),name='featured-random-list'),
    url(r'^category-product-list/$', views_api.ProductCategoryListView.as_view(),name='category-product-list'),
    url(r'^category-list/$', views_api.CategoryListView.as_view(),name='category-list'),
    ]