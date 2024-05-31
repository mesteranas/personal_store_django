from rest_framework import serializers
from home import models
class items(serializers.ModelSerializer):
    class Meta:
        model=models.item
        fields = ['id', 'name', 'description', 'price', 'summery', 'image', 'buyCount', 'category', 'date', 'itemsCount', 'information']
class Comments(serializers.ModelSerializer):
    class Meta:
        model=models.comment
        fields=["id","content","Item","user","date"]