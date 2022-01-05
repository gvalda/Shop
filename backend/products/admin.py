from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = [
        'title',
        'price'
    ]


admin.site.register(Product, ProductAdmin)
