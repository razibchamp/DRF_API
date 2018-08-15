from rest_framework import serializers
from .models import Meal, Order
from django.db.models import Sum

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'cost')
        # depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        meals = MealSerializer(read_only=True, many=True)
        fields = ('id', 'name', 'meals')
        # depth = 1
        

class OrderListSerializer(serializers.ModelSerializer):

    total_cost = serializers.SerializerMethodField(read_only=True)

    def get_total_cost(self, order):
        cost = Meal.objects.filter(
            order=order
        ).aggregate(Sum('cost'))["cost__sum"]
        return cost if cost is not None else 0.00


    class Meta:
        model = Order
        meals = MealSerializer(read_only=True, many=True)
        fields = ('id', 'name', 'meals', 'total_cost')
        depth = 1
