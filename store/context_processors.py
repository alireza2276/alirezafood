from .models import Category, Category, Product
from cart.cart import Cart
from django.db.models import Count
from core.models import Information




def cart(request):
    return {'cart': Cart(request)}


def show_category(request):
    category = Category.objects.order_by('title')
    return {'category': category}

def count_likes(request):
    products = Product.objects.order_by('-likes').exclude(category__title__icontains='نوشیدنی').annotate(likes_count=Count('likes'))[:6]
    percentages = Product.objects.order_by('-likes').exclude(category__title__icontains='نوشیدنی').annotate(likes_count=Count('likes')).all()

    return {'products': products, 'percentages': percentages}

def show_information(request):
    information = Information.objects.all().last()
    return {'information': information}