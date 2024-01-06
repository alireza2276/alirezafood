from .models import Category, Category, Product
from cart.cart import Cart
from django.db.models import Count




def cart(request):
    return {'cart': Cart(request)}


def show_category(request):
    category = Category.objects.order_by('title')
    return {'category': category}

def count_likes(request):
    products = Product.objects.order_by('-likes').exclude(category__title__icontains='نوشیدنی').annotate(likes_count=Count('likes'))[:3]
    return {'products': products}
