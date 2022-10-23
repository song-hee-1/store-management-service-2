from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.orders.models import Order
from apps.orders.serializers import OrderCreateSerializer, OrderListSerializer
from apps.products.models import Product


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        else:
            return OrderListSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        product = data['product']

        total_price = 0

        if product:
            try:
                product_id = product.id
                total_price = Product.objects.get(id=product_id).price
            except Exception as e:
                message = {f"ERROR: 에러가 발생하였습니다. {e}"}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer, total_price)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, total_price=None):
        serializer.save(total_price=total_price)
