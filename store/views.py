from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 6
    


def category(request, pk=None):
    categories = get_object_or_404(Category, id=pk)
    products = categories.products.all()
    return render(request, 'product_list.html', context={
        'categories': categories,
        'products': products
    })


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

