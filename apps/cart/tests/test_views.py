from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from apps.accounts.models import User
from apps.products.models import Product
from apps.cart.models import Cart, CartItem


class CartViewSetTest(APITestCase):
    """ Cart ViewSet이 정상작동하는지 확인하기 위한 테스트 """

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
            price= 28700,
            stock= 100
        )

        self.product2 = Product.objects.create(
            name="실속세트 3종",
            description="유기농 순면 커버 생리대 중형(4P) 5팩, 대형(4P) 3팩, 오버나이트(2P) 3팩",
            price=23300,
            stock=100
        )

        self.cart = Cart.objects.create(
            user_id=self.user.id
        )

        CartItem.objects.create(
            quantity=1,
            cart_id = self.cart.id,
            product_id = self.product.id
        )

    def test_cart_get_list(self):
        response = self.client.get(reverse('cart-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_cart_get_retrieve(self):
        response = self.client.get(reverse('cart-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_cart_update_fail(self):
        update_data = {
            "cart_total": 1000000
        }
        response = self.client.patch(reverse('cart-detail', kwargs={'pk': 1}), update_data)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_cart_update_fail(self):
        response = self.client.delete(reverse('cart-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class CartItemViewSetTest(APITestCase):
    """ Cart에 제품 추가, 수량 조절, 삭제가 정상작동하는지 확인하기 위한 테스트 """

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

        self.product2 = Product.objects.create(
            name="실속세트 3종",
            description="유기농 순면 커버 생리대 중형(4P) 5팩, 대형(4P) 3팩, 오버나이트(2P) 3팩",
            price=23300,
            stock=100
        )

        self.cart = Cart.objects.create(
            user_id=self.user.id
        )

        CartItem.objects.create(
            quantity=1,
            cart_id=self.cart.id,
            product_id=self.product.id
        )

    def test_add_product_cart(self):
        data = {
            "quantity": 1,
            "cart": self.cart.id,
            "product": self.product2.id
        }
        response = self.client.post(reverse('cart-item-list'), data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_modify_cart_product_quantity(self):
        update_data = {
                "quantity": 2
        }
        response = self.client.patch(reverse('cart-item-detail', kwargs={'pk': 1}), update_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['quantity'] == 2)

    def test_delete_cart_product(self):
        response = self.client.delete(reverse('cart-item-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
