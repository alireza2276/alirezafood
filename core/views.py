from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from store.models import Product
from django.db.models import Count
from django.contrib import messages
from .models import Contact
from django.utils.translation import gettext_lazy as _



def home(request):
    
    return render(request, 'home.html' )


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message, phone=phone, subject=subject)
        messages.success(request, _('Your message succefully added'))

        return render(request, 'contact.html', context={
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message
        })
    
        
    
    
    return render(request, 'contact.html')


def search(request):
    q = request.GET.get('q')
    products = Product.objects.filter(title__icontains=q)
    return render(request, 'product_list.html', context={'products': products})
