from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

from django.contrib import messages

from .models import Agent
from apps.common.models import SubEmail


@method_decorator(login_required, name='dispatch')
class AboutPageView(View):
    def get(self, request):
        agents = Agent.objects.filter(role=Agent.Role.AGENT).order_by('id')[:4]
        return render(request, 'about.html', context={'agents': agents})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            SubEmail.objects.create(name=name, email=email)
            messages.success(request, 'You have successfully subscribed to our newsletter!')
            return redirect('about')
