from rest_framework import serializers

from apps.orders.models import Order, OrderItem
from apps.products.models import Product
from apps.cart.serializers import SimpleProductSerializers


class OrderItemSimpleSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializers(many=False)

    class Meta:
        model = OrderItem
        exclude = ['id', 'create_at']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['order_state', 'total_price']


# class OrderProductNestedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'description', 'price']


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemSimpleSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['product_info'] = OrderProductNestedSerializer(instance.product).data
    #     return response
