from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from . models import Stock
from . serializer import StockSerializer

# Create your views here.


def index(request):
    return render(request,'index.html')

class StockList(APIView):
    
    def get(self,request):
        sttocks=Stock.objects.all()
        serilalizers=StockSerializer(sttocks,many=True)
        return Response(serilalizers.data)
