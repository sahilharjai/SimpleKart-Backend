from rest_framework import serializers

from .models import Cart,CartItem
from products.serializers import VariationDetailSerializer
from products.models import Variation,Product

class CartDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'



class UserCartSerializer(serializers.ModelSerializer):
	item=serializers.SerializerMethodField()
	cart = CartDetailSerializer(many=False,read_only=True)
	class Meta:
		model = CartItem
		fields = '__all__'

	def get_item(self,obj):
		variation = Variation.objects.get(id=obj.item.id)		
		serializer = VariationDetailSerializer(variation,many=False,read_only=True,context={'request':self.context['request']})
		return serializer.data







