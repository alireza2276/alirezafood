from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart_view, name='cart_add'),
    path('remove/<int:product_id>/', views.remove_from_cart_view, name='remove_cart'),
    path('clear/', views.cart_clear, name='cart_clear'),
    path('checkout/', views.order_create, name='order_create')
    
]