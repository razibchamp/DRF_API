from rest_framework import serializers
from .models import Meal, Order

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
    class Meta:
        model = Order
        meals = MealSerializer(read_only=True, many=True)
        fields = ('id', 'name', 'meals')
        depth = 1