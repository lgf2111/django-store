from django.contrib import admin
from .models import Product, ProductImage, Rating

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Rating)