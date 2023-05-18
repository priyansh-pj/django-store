from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.Serializer):
    id = serializers.UUIDField()
    name= serializers.CharField()
    description = serializers.CharField()

    class Meta:
        fields = ('id','name','description')

class ItemsSerializers(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    class Meta:
        fields = ('id','name', 'description', 'quantity')