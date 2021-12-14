from django.db import models

# Create your models here.
class news(models.Model):
    title= models.CharField(max_length=200)
    link =models.CharField(max_length=2089 ,default="",unique=True)
    published =models.DateTimeField()
    created =models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    source =models.CharField(max_length=30,default="",blank=True ,null=True)