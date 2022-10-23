from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from apps.orders.models import Order
from apps.orders.serializers import OrderCreateSerializer, OrderListSerializer
from apps.products.models import Product


class OrderViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Order.objects.all()
        order_state = self.request.GET.get('order_state', '')
        start_date = self.request.GET.get('start_date', '')
        end_date = self.request.GET.get('end_date', '')

        if order_state:
            queryset = queryset.filter(order_state=order_state)

        if start_date:
            queryset = queryset.filter(order_date__gte=start_date)

        if end_date:
            queryset = queryset.filter(order_date__lte=end_date)

        return queryset

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
                response = {'ERROR': f'에러가 발생하였습니다. {e}'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer, total_price)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        """ DELETE 메소드는 허용하지 않습니다. """
        response = {'ERROR': 'DELETE 메소드는 허용하지 않습니다.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer, total_price=None):
        serializer.save(total_price=total_price)
