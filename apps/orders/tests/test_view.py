from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from apps.products.models import Product
from apps.accounts.models import User
from apps.orders.models import Order


class OrderViewSetTest(APITestCase):
    """ Order ViewSet이 정상작동하는지 확인하는 테스트 """

    def setUp(self):
        self.user = User.objects.create_user(
            username="핑핑",
            password="0000",
            email="test@test.com",
            phone_number="010-0000-0001",
            date_of_birth="2018-09-20"
        )
        login_data = {'email': 'test@test.com', 'password': '0000'}
        response = self.client.post(reverse('rest_login'), login_data)
        access_token = response.data["access_token"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.product = Product.objects.create(
            name="알짜세트 4종",
            description="팬티라이너(20P) 2팩, 중형(4P) 4팩, 대형(4P) 3팩, 오버나이트(2P) 3팩",
            price=28700,
            stock=100
        )

        self.order = Order.objects.create(
            address="핑핑군 핑핑면 핑핑리",
            receiver_name="핑핑",
            receiver_phone_number="010-0000-0001",
            user=self.user,
            product=self.product,
            product_quantity=1
        )

    def test_order_delete_fail(self):
        response = self.client.delete(reverse('order-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_order_get_retrieve_product_info(self):
        response = self.client.get(reverse('order-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['product_info']['id'] == 1)
        self.assertTrue(response.data['product_info']['name'] == "알짜세트 4종")
        self.assertTrue(response.data['product_info']['price'] == 28700)
