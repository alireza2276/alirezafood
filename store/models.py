from django.db import models
from django.urls import reverse



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

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modeified = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    
