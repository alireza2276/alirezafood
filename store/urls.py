from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<int:pk>/', views.category, name='category'),
    path('likes/<int:pk>/', views.likeview, name='likes' ),
    path('comments/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),
]
