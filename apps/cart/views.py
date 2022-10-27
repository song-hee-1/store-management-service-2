from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.cart.models import Cart, CartItem
from apps.cart.serializers import CartListSerializer, CartCreateSerializer, CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CartListSerializer
        elif self.action == "create":
            return CartCreateSerializer
        else:
            return CartListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def update(self, request, *args, **kwargs):
        response = {'ERROR': 'UPDATE 메소드는 허용하지 않습니다.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        response = {'ERROR': 'DELETE 메소드는 허용하지 않습니다.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
