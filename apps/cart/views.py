from django.shortcuts import get_object_or_404, redirect, render

from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from .models import Cart, CartItem, Order, OrderItem
from apps.product.models import Product
from apps.common.models import SubEmail


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def get(self, request, pk):
        cart_item = get_object_or_404(CartItem, id=pk, cart__user=request.user)
        cart = cart_item.cart
        cart_item.delete()
        messages.success(request, "Item removed from cart")
        other_items = CartItem.objects.filter(cart=cart).exists()
        if not other_items:
            cart.delete()
            messages.info(request, "Cart deleted because it was empty")
            return redirect('home')


@method_decorator(login_required, name='dispatch')
class CartPageView(View):
    def get(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_total_price = cart.cart_total_price
        cart_sub_total_price = cart.cart_sub_total_price

        context = {
            "cart": cart,
            "cart_items": cart_items,
            "cart_total_price": cart_total_price,
            "cart_sub_total_price": cart_sub_total_price,
        }

        return render(request, "cart.html", context)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")

        if name and email:
            sub_email = SubEmail()
            sub_email.name = name
            sub_email.email = email
            sub_email.save()
            messages.success(request, "Your email has been added to our mailing list.")
            return redirect("cart")


@method_decorator(login_required, name='dispatch')
class OrderPageView(View):
    def get(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total = cart.cart_total_price

        context = {
            'cart': cart,
            'cart_items': cart_items,
            'total': total,
        }

        return render(request, "checkout.html", context)

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        name = request.POST.get('name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        notes = request.POST.get('notes', "")

        if name and email:
            SubEmail.objects.get_or_create(name=name, email=email)
            messages.success(request, "Your email has been added to our mailing list.")
            return redirect("order")

        if first_name and last_name and email and phone_number and address:
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                notes=notes,
            )
            order.save()
            messages.success(request, "Your order has been created.")
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.discount,
                )
            cart.delete()
            messages.success(request, "Your order has been placed successfully!")
            return redirect('thank-you')
        else:
            messages.error(request, "Please fill in all fields.")
            return redirect("order")
