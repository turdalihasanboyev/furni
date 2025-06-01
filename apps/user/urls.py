from django.urls import path

from .views import RegisterPageView, LoginPageView, LogoutView, ThankYouPageView


urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('thank-you/', ThankYouPageView.as_view(), name='thank-you'),
]
