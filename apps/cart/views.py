from django.shortcuts import get_object_or_404, redirect

from django.views import View

from django.contrib import messages

from .models import Cart, CartItem
from apps.product.models import Product


class AddToCartView(View):
    def get(self, request, pk):
        url = request.META.get("HTTP_REFERER")
        product = get_object_or_404(Product, id=pk)
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if cart_created:
            messages.success(request, "Cart created")
        if item_created:
            messages.success(request, "Item added to cart")
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect(url)


class RemoveFromCartView(View):
    def get(self, request, pk):
        url = request.META.get("HTTP_REFERER")
        product = get_object_or_404(Product, id=pk)
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, f"Quantity of {product.name} decreased by 1.")
            else:
                cart_item.delete()
                messages.success(request, f"{product.name} removed from cart.")
                if not CartItem.objects.filter(cart=cart).exists():
                    cart.delete()
                    messages.info(request, "Your cart is now empty and has been deleted.")
        else:
            messages.warning(request, "Item not found in your cart.")
        return redirect(url)
