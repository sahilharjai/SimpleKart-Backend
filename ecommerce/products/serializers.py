from rest_framework import serializers

from .models import Product,Category,ProductFeatured,Variation

class CategoryDetailSerializer(serializers.ModelSerializer):
	# comments = CommentRetrieveSerializer(many=True,read_only=True)
	# likes_count = serializers.SerializerMethodField()
	# is_liked_by_user = serializers.SerializerMethodField()
	# rating_by_user = serializers.SerializerMethodField()
	# product_pic = serializers.SerializerMethodField()
	class Meta:
		model = Category
		fields = '__all__'

	# def get_product_pic(self,obj):
	# 	return self.context['request'].build_absolute_uri(obj.get_image_url())

class VariationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Variation
		fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
	# comments = CommentRetrieveSerializer(many=True,read_only=True)
	# likes_count = serializers.SerializerMethodField()
	# is_liked_by_user = serializers.SerializerMethodField()
	# rating_by_user = serializers.SerializerMethodField()
	variations = serializers.SerializerMethodField()
	product_pic = serializers.SerializerMethodField()
	categories = CategoryDetailSerializer(read_only=True,many=True)
	class Meta:
		model = Product
		fields = '__all__'

	def get_product_pic(self,obj):
		return self.context['request'].build_absolute_uri(obj.get_image_url())

	def get_variations(self,obj):
		variations = Variation.objects.filter(product=obj)
		serializer = VariationSerializer(variations,many=True,read_only=True)
		return serializer.data

	# def get_likes_count(self, obj):
	# 	return len(obj.all_liked_users())

	# def get_is_liked_by_user(self,obj):
	# 	user = self.context['request'].user
	# 	return obj.is_liked_by_user(user=user)

	# def get_rating_by_user(self,obj):
	# 	user = self.context['request'].user
	# 	if user.is_authenticated:
	# 		if user.is_er():
	# 			return obj.average_rating
	# 		else:
	# 			return obj.get_rating_by_user(user)
	# 	return 0

class VariationDetailSerializer(serializers.ModelSerializer):
	product = serializers.SerializerMethodField()
	
	class Meta:
		model = Variation
		fields = '__all__'
	def get_product(self,obj):
		product = Product.objects.get(variations_rev__id=obj.id)
		print(self.context)
		serializer = ProductDetailSerializer(product,many=False,read_only=True,context={'request':self.context['request']})
		return serializer.data


class FeaturedDetailSerializer(serializers.ModelSerializer):
	# comments = CommentRetrieveSerializer(many=True,read_only=True)
	# likes_count = serializers.SerializerMethodField()
	# is_liked_by_user = serializers.SerializerMethodField()
	# rating_by_user = serializers.SerializerMethodField()
	product = ProductDetailSerializer()
	class Meta:
		model = ProductFeatured
		fields = '__all__'

	# def get_product_pic(self,obj):
	# 	return self.context['request'].build_absolute_uri(obj.get_image_url())