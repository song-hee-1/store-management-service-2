from rest_framework import viewsets

from apps.orders.models import Order
from apps.orders.serializers import OrderCreateSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

