from django.db import models
from django.contrib.auth.models import User
from . import dictionarys
def getImagePath(instance,fileName):
    return "images/{}/{}".format(str(instance.pk),fileName)
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
    price=models.FloatField(max_length=1000)
    summery=models.CharField(max_length=500)
    image=models.ImageField(upload_to=getImagePath)
    buyCount=models.IntegerField()
    category=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now=True)
    itemsCount=models.IntegerField()
    information=models.TextField()
    def __str__(self):
        return self.name
class comment(models.Model):
    content=models.TextField()
    Item=models.ForeignKey(to=item,on_delete=models.CASCADE)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username+str(self.date)