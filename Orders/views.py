import random
import string
from django.shortcuts import render

from .models import User
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import Orders
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def placeOrder(request):
    if request.method == 'POST':
        new_order = JSONParser().parse(request)
        if new_order is not None:
            serializer = None
            id = ''.join(random.choice(string.digits) for _ in range(6))
            print (new_order)
            print (id)
            # new_order(orderid)=id
            serializer = OrderSerializer(data=new_order, many=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False,  status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'No orders found!'}, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class ViewOrders(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']