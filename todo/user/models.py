from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField()
    last_name=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    occupation=models.CharField(max_length=20)



