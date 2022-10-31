from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # order 필드때문에 product의 3건의 데이터를 가져오기 위하여 추가적인 쿼리가 발생하므로,
        # order 필드를 제외하거나 viewset의 queryset을 prefetch_related()를 이용하여 최적화 가능
        # exclude = ['order']
