from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from apps.accounts.models import User


class ProductViewSetTest(APITestCase):
    """ Product ViewSet이 정상작동하는지 확인하는 테스트 """

    def setUp(self):
        User.objects.create_user(
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

        data = {
            "name": "실속세트 3종",
            "description": "중형(4P) 5팩, 대형(4P) 3팩, 오버나이트(2P) 3팩",
            "price": 23300,
            "stock": 100
        }

        response = self.client.post(reverse('products-list'), data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_product_create(self):
        data = {
            "name": "알짜세트 4종",
            "description": "팬티라이너(20P) 2팩, 중형(4P) 4팩, 대형(4P) 3팩, 오버나이트(2P) 3팩",
            "price": 28700,
            "stock": 100
        }

        response = self.client.post(reverse('products-list'), data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_product_get_list(self):
        response = self.client.get(reverse('products-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_product_get_retrieve(self):
        response = self.client.get(reverse('products-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_product_update(self):
        update_data = {
            "name": "알짜세트 4종 이름 수정 테스트"
        }
        response = self.client.patch(reverse('products-detail', kwargs={'pk': 1}), update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['name'] == "알짜세트 4종 이름 수정 테스트")

    def test_product_destory(self):
        response = self.client.delete(reverse('products-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
