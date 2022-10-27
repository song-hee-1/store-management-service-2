from django.urls import path, include

from rest_framework import routers

from apps.cart.views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register('carts', CartViewSet, basename='cart')
router.register('cart-items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
]
