from django.shortcuts import render, redirect

from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout

from .models import CustomUser
from apps.common.models import SubEmail


class RegisterPageView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = CustomUser.objects.create_user(email=email, password=password)
        messages.success(request, 'User created successfully')
        login(request, user)
        return redirect('home')


class LoginPageView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'User logged out successfully')
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class ThankYouPageView(View):
    def get(self, request):
        return render(request, 'thankyou.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            SubEmail.objects.create(name=name, email=email)
            messages.success(request, 'Thank you for your email')
            return redirect('thank-you')
