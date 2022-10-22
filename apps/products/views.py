from rest_framework import viewsets

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProudctViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
