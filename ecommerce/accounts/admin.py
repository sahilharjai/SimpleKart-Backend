from django.contrib import admin

# Register your models here.
from .models import User,UserAddress,Order

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(Order)