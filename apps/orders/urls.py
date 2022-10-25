from django.urls import path, include

from rest_framework import routers

from apps.orders.views import OrderViewSet, OrderSQLSumView, OrderORMSumView

router = routers.DefaultRouter()
router.register('', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/v1', OrderSQLSumView.as_view()),
    path('summary/v2', OrderORMSumView.as_view()),
]
