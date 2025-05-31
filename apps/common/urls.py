from django.urls import path

from .views import HomePageView, ShopPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopPageView.as_view(), name='shop'),
]
