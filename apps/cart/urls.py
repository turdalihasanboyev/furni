from django.urls import path

from .views import AddToCartView, RemoveFromCartView


urlpatterns = [
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
