from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=70)
    
