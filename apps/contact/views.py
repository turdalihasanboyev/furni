from django.shortcuts import render, redirect

from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from .models import Contact
from apps.common.models import SubEmail


@method_decorator(login_required, name='dispatch')
class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if first_name and last_name and email and message:
            contact = Contact()
            contact.first_name = first_name
            contact.last_name = last_name
            contact.email = email
            contact.message = message
            contact.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')

        if name and email:
            sub_email = SubEmail()
            sub_email.name = name
            sub_email.email = email
            sub_email.save()
            messages.success(request, 'Your email has been added successfully.')
            return redirect('contact')
