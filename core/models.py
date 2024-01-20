from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    

class Information(models.Model):
    address = models.CharField(max_length=255)
    time_working = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
