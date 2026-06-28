from django.db import models

# Create your models here.
class UserRegister(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)