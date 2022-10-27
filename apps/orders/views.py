from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from apps.orders.models import Order
from apps.orders.serializers import OrderCreateSerializer, OrderListSerializer
from apps.products.models import Product

from django.db.models import Sum
from django.db import connection


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


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

    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #
    #     product = data['product']
    #     product_quantity = data['product_quantity']
    #
    #     total_price = 0
    #
    #     if product:
    #         try:
    #             product_id = product.id
    #             product_price = Product.objects.get(id=product_id).price
    #             total_price = product_price * product_quantity
    #         except Exception as e:
    #             response = {'ERROR': f'에러가 발생하였습니다. {e}'}
    #             return Response(response, status=status.HTTP_400_BAD_REQUEST)
    #
    #     self.perform_create(serializer, total_price)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        """ DELETE 메소드는 허용하지 않습니다. """
        response = {'ERROR': 'DELETE 메소드는 허용하지 않습니다.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def perform_create(self, serializer, total_price=None):
    #     serializer.save(total_price=total_price)


class OrderSQLSumView(APIView):

    def get(self, request):
        """
        일자별 총 매출 SQL :

        SELECT (date("order".order_date)) AS day, SUM("order".total_price) AS day_total_sales
        FROM "order"
        WHERE "order".order_state="주문완료"
        GROUP BY day
        ORDER BY day ASC


        일자별 제품별 판매 수량 SQL:

        SELECT (date(order_date)) AS day, "order".product_id,
        SUM("order".product_quantity)  AS sales_quantity_per_product
        FROM "order"
        WHERE "order".order_state = "주문완료"
        GROUP BY "order".product_id, day
        ORDER BY day ASC

        일자별 제품별 매출 SQL :

        SELECT (date(order_date)) AS day, "order"."product_id", SUM("order"."total_price") AS sales_per_product
        FROM "order"
        WHERE "order"."order_state" = "주문완료"
        GROUP BY "order"."product_id", day
        ORDER BY "day" ASC
        """

        total_sales_query = 'SELECT (date("order".order_date)) AS day, ' \
                            'SUM("order".total_price) AS day_total_sales ' \
                            'FROM "order" ' \
                            'WHERE "order".order_state="주문완료" ' \
                            'GROUP BY day ' \
                            'ORDER BY day ASC'

        sales_quantity_per_product_query = 'SELECT (date(order_date)) AS day, ' \
                                           '"order".product_id, SUM("order".product_quantity)  ' \
                                           'AS sales_quantity_per_product ' \
                                           'FROM "order" ' \
                                           'WHERE "order".order_state = "주문완료" ' \
                                           'GROUP BY "order".product_id, day ' \
                                           'ORDER BY day ASC'

        sales_per_product_query = 'SELECT (date(order_date)) AS day, ' \
                                  '"order"."product_id", ' \
                                  'SUM("order"."total_price") AS sales_per_product ' \
                                  'FROM "order" ' \
                                  'WHERE "order"."order_state" = "주문완료" ' \
                                  'GROUP BY "order"."product_id", day ' \
                                  'ORDER BY "day" ASC'

        cursor = connection.cursor()
        result = cursor.execute(total_sales_query)
        day_total_sales = dictfetchall(cursor)

        result = cursor.execute(sales_quantity_per_product_query)
        sales_quantity_per_product = dictfetchall(cursor)

        result = cursor.execute(sales_per_product_query)
        sales_per_product = dictfetchall(cursor)

        data = day_total_sales, sales_quantity_per_product, sales_per_product

        return Response(data)


class OrderORMSumView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders/summary_index.html'

    def get(self, request):
        order_per_date = Order.objects.filter(order_state="주문완료").extra(select={'day': 'date(order_date)'})

        total_sales = order_per_date.\
            values('day').\
            order_by('day').\
            annotate(day_total_sales=Sum('total_price'))

        sales_per_product = order_per_date.\
            values('day', 'product_id').\
            order_by('day').\
            annotate(sales_quantity_per_product=Sum('product_quantity'), sales_per_product=Sum('total_price'))

        return Response({'total_sales': total_sales, 'sales_per_product': sales_per_product})
