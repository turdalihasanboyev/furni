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
        'discount_price',
        'price_type',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
