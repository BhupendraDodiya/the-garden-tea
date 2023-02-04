from django.db import models

# Create your models here.
class info(models.Model):
    Name = models.CharField(max_length=100) 
    Email = models.EmailField() 
    Subject = models.CharField(max_length=100) 
    Message = models.TextField() 