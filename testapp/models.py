from django.db import models

# Create your models here.
class User(models.Model):
    User_Name=models.CharField(max_length=64)
    User_Pwd=models.CharField(max_length=10)