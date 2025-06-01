from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

from django.contrib import messages

from apps.product.models import Product
from .models import SubEmail
from apps.agent.models import Agent
from apps.blog.models import Article


@method_decorator(login_required, name='dispatch')
class HomePageView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-created_at')[:3]
        testimonials = Agent.objects.filter(role=Agent.Role.TESTIMONIAL).order_by('id')[:3]
        articles = Article.objects.all().order_by('-created_at')[:3]

        context = {
            'products': products,
            'testimonials': testimonials,
            'articles': articles,
        }

        return render(request, 'index.html', context)

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')

        if name and email:
            SubEmail.objects.create(name=name, email=email)
            messages.success(request, 'Your email has been added to our list.')
            return redirect ('home')


@method_decorator(login_required, name='dispatch')
class ShopPageView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-created_at')[:8]
        return render(request, 'shop.html', context={'products': products})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            SubEmail.objects.create(name=name, email=email)
            messages.success(request, 'Your email has been added to our list.')
            return redirect('shop')
