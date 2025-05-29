from django.db import models

from apps.common.models import BaseModel


class Cart(BaseModel):
    is_completed = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.SET_NULL, null=True, related_name='cart_user')
    session_id = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    @property
    def total(self):
        return sum(item.total_price for item in self.cart_item_cart.all())

    @property
    def items_count(self):
        return self.cart_item_cart.count()

    def __str__(self):
        return f"Cart {self.id} ({self.user})"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item_cart")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="cart_item_product")
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    @property
    def total_price(self):
        return int(self.product.discount_price * self.quantity)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Order(BaseModel):
    STATUS = (
        ('new', 'New'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey('user.CustomUser', on_delete=models.SET_NULL, null=True, related_name='order_user')
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    @property
    def total(self):
        return sum(item.total_price for item in self.order_item_order.all())

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_item_order")
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True, related_name='order_item_product')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    @property
    def total_price(self):
        return int(self.price * self.quantity)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.price})"
