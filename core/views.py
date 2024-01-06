from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from store.models import Product
from django.db.models import Count


def home(request):
    
    return render(request, 'home.html' )