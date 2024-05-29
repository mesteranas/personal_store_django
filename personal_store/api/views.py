from django.shortcuts import render,get_object_or_404
from home import models
from . import serializers
from rest_framework import generics,status,response
from rest_framework.views import APIView
# Create your views here.
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
        return response.Response(ser.data)