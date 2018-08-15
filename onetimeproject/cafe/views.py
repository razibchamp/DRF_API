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

    # def create(self, request):
    #     # order = self.get_object()
    #     # queryset = Order.objects.all()
    #     serializer = OrderSerializer(data=request.data)
        
    #     if serializer.is_valid():
            
    #         serializer.save()
    #         # serializer.annotate(total_cost=Sum('cost'))
    #         # serializer.save()
    #         return Response(serializer.data)
    #         # order.total_cost = order.meals.aggregate(Sum('cost'))
    #         # print(cost)
    #         # order.add(total_cost=cost)
    #         # order.save()
    #         # serializer = OrderSerializer(data=order)
    #         # return Response(serializer.data)

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Order.objects.filter(pk=pk)
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)