from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    subject = models.CharField(max_length=100) 
    message = models.TextField() 

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    upload_photo = models.ImageField(upload_to="product/")