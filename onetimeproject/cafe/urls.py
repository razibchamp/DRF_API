from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meals', views.MealView)
router.register('orders', views.OrderView)
# router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]