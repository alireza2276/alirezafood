from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/image-category', blank=True)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(default=0)
    discount = models.PositiveBigIntegerField(default=0, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static/product-image')
    status = models.BooleanField(default=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_likes', blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modeified = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.title}"
    
    
    def total_likes(self):
        return self.likes.count()

    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    

    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    
    full_name= models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    email = models.EmailField()
    order_notes = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modeified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.full_name}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()


    
