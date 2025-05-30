from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'price',
        'percentage',
        'discount',
        'price_type',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
