from django.contrib import admin
from .models import Product, Category, Customer, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'datetime_created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'birth_date']


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'quantity', 'product', 'price']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'full_name', 'datetime_created', 'status', 'address', 'phone_number']
    inlines = [OrderItemTabularInline]



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    
    