from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
class Course(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    decription = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(null=True)
    uploaded_date = models.DateTimeField(null=True)
    active = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    