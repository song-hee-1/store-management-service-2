from rest_framework import serializers

from apps.products.models import Product
from apps.cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class SimpleProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSimpleSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializers(many=False)
    sub_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "sub_total"]

    def get_sub_total(self, CartItem):
        return CartItem.quantity * CartItem.product.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSimpleSerializer(many=True)
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'cart_total', 'create_at']

    def get_cart_total(self, Cart):
        items = Cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
