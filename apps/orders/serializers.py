from rest_framework import serializers

from apps.orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['order_state', 'total_price']


