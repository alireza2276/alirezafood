from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Count



class ProductList(ListView):
    queryset = Product.objects.order_by('title').exclude(category__title__icontains='نوشیدنی').annotate(likes_count=Count('likes'))
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


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product.objects.select_related('category'), id=self.kwargs['pk'])
        related_products = Product.objects.filter(category=product.category).exclude(id=self.kwargs['pk'])[:3]
        context['related_products'] = related_products

        stuff = get_object_or_404(Product, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked


        return context

# Like Product
@login_required
def likeview(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))

    liked = False

    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
        liked = False
    else:
        product.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('product_detail', args=[str(pk)]))