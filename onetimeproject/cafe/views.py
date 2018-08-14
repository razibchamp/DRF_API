from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Order
from .serializers import OrderListSerializer, MealSerializer, OrderSerializer
from rest_framework.response import Response
# Create your views here.

class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)