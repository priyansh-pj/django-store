from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render,redirect
from .models import *
from .serializers import *

# Create your views here.
def store_landing(request):
    data = {
        "data" : Category.objects.all()
    }
    return render(request, "index.html", data)

def items(request,id):
    data = {
        "data": Item.objects.filter(owner = id)
    }
    return render(request, "item.html", data)

def checkout(request,id):
    data = Item.objects.get(id = id)
    print(data.quantity)
    if(data.quantity > 0):
        Item.objects.filter(id=id).update(quantity=data.quantity-1)

    return redirect('landing')

@api_view(['GET'])
def api_category(request):
    category = Category.objects.all()
    serializer = CategorySerializers(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_items(request):
    items = Item.objects.all()
    serializer = ItemsSerializers(items, many=True)
    return Response(serializer.data)



