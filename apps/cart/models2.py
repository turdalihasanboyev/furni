from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Cart(BaseModel):
    user = models.OneToOneField(
        'user.CustomUser', on_delete=models.CASCADE, related_name='cart_user')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"Cart ({self.user})"


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_item_cart")
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name='cart_item_product')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    @property
    def total_price(self):
        return self.product.discount * self.quantity

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

    user = models.ForeignKey(
        'user.CustomUser', on_delete=models.CASCADE, related_name='order_user')
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    notes = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    @property
    def total(self):
        return sum(item.total_price for item in self.order_item_order.all())

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name}"


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_item_order')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, related_name='order_item_product')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.price})"


class Wishlist(BaseModel):
    user = models.OneToOneField(
        'user.CustomUser', on_delete=models.CASCADE, related_name='wishlist_user')

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    @property
    def total_items(self):
        return self.wishlist_item_wishlist.count()

    def __str__(self):
        return f"Wishlist ({self.user})"


class WishlistItem(BaseModel):
    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE, related_name='wishlist_item_wishlist')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, related_name='wishlist_item_product')

    class Meta:
        unique_together = ('wishlist', 'product')
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'

    def __str__(self):
        return f"{self.product.name} in Wishlist {self.wishlist.id}"
