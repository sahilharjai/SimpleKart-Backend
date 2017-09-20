from rest_framework import serializers
from datetime import datetime

from .models import User,UserAddress,Order
from carts.serializers import UserCartSerializer
from carts.models import CartItem



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','mobile','password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        time = datetime.now()
        user.username = str(user.email)[-5:]+str(str(time).split(".")[0])[-5:]
        user.save()     
        return user







class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('__all__')

    




class UserDetailSerializer(serializers.ModelSerializer):
	user_address = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ('__all__')

	def get_user_address(self,obj):
		user_address = UserAddress.objects.filter(user=obj)
		serializer = UserAddressSerializer(user_address,many=True,read_only=True)
		return serializer.data




class UserOrderSerializer(serializers.ModelSerializer):
	user = UserRegistrationSerializer(many=False,read_only=True)
	shipping_address = UserAddressSerializer(many=False,read_only=True)
	cart_item = serializers.SerializerMethodField()
	class Meta:
		model = Order
		fields = ('__all__')

	def get_cart_item(self,obj):
		cart_item = CartItem.objects.filter(cart=obj.cart)
		serializer = UserCartSerializer(cart_item,many=True,read_only=True,context={'request':self.context['request']})
		return serializer.data
