from django.contrib import admin

from .models import (
    ProductCategory, ProductSubCategory, Product, ProductDetail)

admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(Product)
admin.site.register(ProductDetail)
