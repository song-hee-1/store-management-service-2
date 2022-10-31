from rest_framework import viewsets

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProudctViewset(viewsets.ModelViewSet):
    # prefetch_related를 사용하여 연관된 데이터를 모두 가져옴
    queryset = Product.objects.all().prefetch_related('order')
    serializer_class = ProductSerializer
