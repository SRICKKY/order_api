from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework import viewsets

class OrderView(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer