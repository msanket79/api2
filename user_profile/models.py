from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200,default='')
    last_name=models.CharField(max_length=200,default='')
    phone=models.CharField(max_length=200,default='')
    city=models.CharField(max_length=200,default='')

    def __str__(self) -> str:
        return self.first_name
# Create your models here.


