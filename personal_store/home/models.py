from django.db import models
from django.contrib.auth.models import User
from . import dictionarys
# Create your models here.
class Profile (models.Model):
    gender=models.CharField(choices={"male":"male","female":"female"},default="male",max_length=20)
    country=models.CharField(max_length=10,choices=dictionarys.countries,default="us")
    currency=models.CharField(max_length=10,choices=dictionarys.currencies,default="USD")
    user=models.OneToOneField(User,models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.user.first_name,self.user.last_name)
class item(models.Model):
    name=models.CharField(max_length=1000)
    description=models.TextField()
    priceUSD=models.FloatField(max_length=1000)
    summery=models.CharField(max_length=500)
    image=models.ImageField()