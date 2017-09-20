from django.contrib import admin

# Register your models here.

from .models import Product,Category,ProductImage,ProductFeatured,Variation

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductFeatured)
admin.site.register(Variation)