from django.contrib import admin
from .models import *
# Register your models here.

@admin.register((Contact))
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

@admin.register((Product))
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id','name','description','upload_photo']