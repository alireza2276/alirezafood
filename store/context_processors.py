from .models import Category


def show_category(request):
    category = Category.objects.order_by('title')
    return {'category': category}