from django.urls import path

from .views import AddToCartView, RemoveFromCartView, CartPageView, OrderPageView


urlpatterns = [
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('order/', OrderPageView.as_view(), name='order'),
]
