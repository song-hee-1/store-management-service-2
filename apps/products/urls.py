from django.urls import path, include

from rest_framework import routers

from apps.products.views import ProudctViewset

router = routers.DefaultRouter()
router.register('products', ProudctViewset, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
