from django.shortcuts import render,get_object_or_404
from home import models
from . import serializers
from rest_framework import generics,status,response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.models import Token
# Create your views here.
def is_auth(r):
    apiKey=r.data["api"]
    token=get_object_or_404(Token,key=apiKey)
    return token.user
class viewItems(APIView):
    def getCategory(self):
        categories=["all"]
        for item in models.item.objects.all().order_by("-date"):
            List=item.category
            if List in categories:
                continue
            categories.append(List)
        return categories

    def post(self,r):
        data=r.data
        try:
            if data["category"]=="all":
                model=models.item.objects.all().order_by("-"+data["sort"])
            else:
                model=models.item.objects.filter(category=data["category"]).order_by("-"+data["sort"])
        except:
            return response.Response({"data":[],"categories":[]},status=status.HTTP_400_BAD_REQUEST)
        ser=serializers.items(model,many=True)
        return response.Response({"data":ser.data,"categories":self.getCategory()})

class Comments(APIView):
    def post(self,r):
        data=r.data
        try:
            ItemModel=get_object_or_404(models.item,pk=data["pk"])
            model=models.comment.objects.filter(Item=ItemModel).order_by("-date")
        except:
            return response.Response([],status=status.HTTP_400_BAD_REQUEST)
        ser=serializers.Comments(model,many=True)
        for item in ser.data:
            user=get_object_or_404(models.User,pk=item["user"])
            item["user"]=user.first_name + " " + user.last_name

        return response.Response(ser.data)
class CreateNewAccount(APIView):
    def post(self,r):
        data=r.data
        if not User.objects.filter(username=data["username"]).exists():
            user=User.objects.create_user(username=data["username"],email=data["email"],password=data["password"],first_name=data["first_name"],last_name=data["last_name"])
            profile=models.Profile(user=user,gender=data["gender"],country=data["country"],currency=data["currency"],address=data["address"])
            profile.save()
            token,created=Token.objects.get_or_create(user=user)
            return response.Response({"code":0,"token":token.key})
        return response.Response({"code":1},status=status.HTTP_400_BAD_REQUEST)
class login(APIView):
    def post(self,r):
        data=r.data
        user=auth.authenticate(username=data["username"],password=data["password"])
        if user:
            token,created=Token.objects.get_or_create(user=user)
            return response.Response({"code":0,"token":token.key})
        return response.Response({"code":1},status=status.HTTP_400_BAD_REQUEST)
class ChangePassword(APIView):
    def post(self,r):
        data=r.data
        user=is_auth(r)
        userModel=get_object_or_404(User,username=user)
        if userModel.check_password(data["currentPassword"]):
            userModel.set_password(data["newPassword"])
            userModel.save()
            return response.Response({"code":0})
        return response.Response({"code":1},status=status.HTTP_400_BAD_REQUEST)
class EditProfile(APIView):
    def post(self,r):
        data=r.data
        user=is_auth(r)
        userModel=get_object_or_404(User,username=user)
        profile=get_object_or_404(models.Profile,user=userModel)
        userModel.first_name=data["firstName"]
        userModel.last_name=data["lastName"]
        userModel.email=data["email"]
        userModel.save()
        profile.country=data["country"]
        profile.currency=data["currency"]
        profile.address=data["address"]
        profile.save()
        profile.save()
        return response.Response({"code":0})
class ViewProfile(APIView):
    def post(self,r):
        user=is_auth(r)
        userModel=get_object_or_404(User,username=user)
        profile=get_object_or_404(models.Profile,user=userModel)
        return response.Response({"firstName":userModel.first_name,"lastName":userModel.last_name,"email":userModel.email,"country":profile.country,"currency":profile.currency,"address":profile.address})
class DeleteAccount(APIView):
    def post(self,r):
        user=is_auth(r)
        userModel=get_object_or_404(User,username=user)
        if userModel.check_password(r.data["password"]):
            userModel.delete()
            return response.Response({"code":0})
        return response.Response({"code":1},status=status.HTTP_400_BAD_REQUEST)