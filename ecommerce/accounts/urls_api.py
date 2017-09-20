from django.conf.urls import url

from . import views_api


urlpatterns = [   
    url(r'^register/$', views_api.Register.as_view(), name='register'),
	url(r'^mobile-check/(?P<mobile>\d+)/$', views_api.CheckUserExistsOrNot.as_view(), name='email-check'),
	url(r'^user-address/(?P<id>\d+)/$', views_api.CreateUserAddressview.as_view(), name='user-address'),
	url(r'^user-detail/(?P<id>\d+)/$', views_api.UserDetailAddressView.as_view(), name='user-detail'),
	url(r'^user-order-create/(?P<id>\d+)/$', views_api.CreateUserOrderview.as_view(), name='user-order-create'),
	url(r'^user-order-retrieve/(?P<id>\d+)/$', views_api.RetriveUserOrderview.as_view(), name='user-order-retrieve'),
    ]


    
