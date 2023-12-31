from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView



def home(request):
    return render(request, 'home.html')