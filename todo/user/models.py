from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField()
    last_name=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    occupation=models.CharField(max_length=20)



class commnets(models.Model) :
    name_user=models.CharField(max_length=20)
    phone_user=models.IntegerField(unique=True)

    email_user=models.CharField( max_length=20)
    sub_user=models.CharField( max_length=100)

    dec_user=models.TextField()
    date_user=models.DateField( auto_now_add=True)

    def __str__(self):
        return f"{self.name_user} ({self.email_user})"
