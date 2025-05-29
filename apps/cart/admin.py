from django.contrib import admin

from .models import Cart, CartItem, Order, OrderItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'is_completed',
        'ip_address',
        'session_id',
        'total',
        'items_count',
        'created_at',
        'updated_at',
    )
    list_display = ('is_completed',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cart',
        'product',
        'quantity',
        'total_price',
        'created_at',
        'updated_at',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'status',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        'created_at',
        'updated_at',
    )
    list_filter = ('status',)
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        'total',
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product',
        'quantity',
        'price',
        'total_price',
        'created_at',
        'updated_at',
    )
