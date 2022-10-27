# store-management-service-2

제품 쇼핑몰을 관리할 수 있는 관리 페이지 서비스


</br>

## 목차

  * [개발 기간](#개발-기간)
  * [프로젝트 개요](#프로젝트-개요)
      - [💭 프로젝트 설명](#-프로젝트-설명)
      - [🧹 사용 기술](#-사용-기술)
      - [📰 모델링](#-모델링)
      - [🛠 API Test](#-api-test)
      - [🔍 SQL](#-sql)

  * [API ENDPOINT](#api-endpoint)
  * [TIL](#til)



</br>

## 개발 기간
**2022.10.21 ~ 2022.10.27** 

</br>
</br>
  
## 프로젝트 개요




#### 💭 프로젝트 설명
**장바구니 기능**과 일자별로 **총 매출, 제품별 판매수량, 제품별 매출**을 볼 수 있는 쇼핑몰 관리 페이지



</br>

#### 🧹 사용 기술 

- **Back-End** : Python, Django, Django REST
Framework, Dj Rest Auth, Django Allauth, Djangorestframework Simplejwt
- **Database** : SQLite
- **ETC** : Git, Github

</br>



#### 📰 모델링


- 실제 모델링


![Untitled (1)](https://user-images.githubusercontent.com/83492367/198299818-549f1b16-d683-4ad3-90eb-9f173a441af6.png)

- 원하던 모델링


![Untitled](https://user-images.githubusercontent.com/83492367/198283163-36192796-823e-4e92-bead-9d210b061e32.png)




</br>

#### 🛠 API Test

![image](https://user-images.githubusercontent.com/83492367/198281536-62661b1a-66fa-4bfb-8bcf-5b9051c24345.png)


**Test Coverage : 87 %**
![image](https://user-images.githubusercontent.com/83492367/198308477-d1176808-e507-4b92-9276-11cb668bb3fa.png)


- 유저(3) : 
	- `username`으로 로그인 시 실패하는 테스트
	-  `email`로 로그인 시 성공하는 테스트
	- JWT Token이 제대로 발급되는지 확인하는 테스트

- 장바구니(7) :
	-  CartViewSet CRUD 확인하는 테스트
	-  CartItemViewSet에 제품 추가, 수량조절, 삭제가 정상 작동하는지 확인하는 테스트

- 주문(2)
	- OrderViewSet Update 실패하는 테스트
	- OrderViewSet에 제품 정보가 잘 포함되는지 확인하는 테스트

- 상품(5)
	- ProductViewSet CRRUD 확인하는 테스트
	

</br>

#### 🔍 SQL


        일자별 총 매출 = SELECT (date("order".order_date)) AS day, 
                      SUM("order".total_price) AS day_total_sales 
                      FROM "order" 
                      WHERE "order".order_state="주문완료" 
                      GROUP BY day 
                      ORDER BY day ASC

        일자별 제품별 판매수량 = SELECT (date(order_date)) AS day, 
                           "order".product_id, SUM("order".product_quantity) 
                            AS sales_quantity_per_product 
                            FROM "order" 
                            WHERE "order".order_state = "주문완료" 
                            GROUP BY "order".product_id, day 
                            ORDER BY day ASC

        일자별 제품별 매출 = SELECT (date(order_date)) AS day, 
                        "order"."product_id", 
                         SUM("order"."total_price") AS sales_per_product 
                         FROM "order" 
                         WHERE "order"."order_state" = "주문완료" 
                         GROUP BY "order"."product_id", day
                         ORDER BY "day" ASC

	

	
</br>

## API ENDPOINT


### accounts - Dj Rest Auth

URL|Method|Description|
|------|---|---|
|api/accounts/password/reset|POST|이메일을 통한 사용자 비밀번호 재설정|
|api/accounts/password/reset/confirm|POST|사용자 비밀번호 재설정 및 새로운 토큰 발급|
|api/accounts/password/change|POST|기존 비밀번호를 통해 비밀번호 재설정|
|api/accounts/login|POST|사용자 로그인(토큰 반환)|
|api/accounts/logout|POST|사용자 로그아웃|
|api/accounts/token/verify|POST|토큰 유효성 확인|
|api/accounts/token/refresh|POST|refresh 토큰을 통한 access 토큰 재발급|
|api/accounts/registration|POST|사용자 회원가입|



### cart



URL|Method|Action|Description|
|------|---|---|---|
|api/carts|GET|List|장바구니 전체 목록 조회|
|api/carts|POST|Create|장바구니 생성|
|api/carts/int:pk|GET|Retrieve|장바구니 세부내역 조회|

* 그 외 update, destory 불가

URL|Method|Action|Description|
|------|---|---|---|
|api/cart-items|GET|List|장바구니 상품 전체 목록 조회|
|api/cart-items|POST|Create|장바구니 상품 생성|
|api/cart-items/int:pk|GET|Retrieve|장바구니 상품 세부내역 조회|
|api/cart-items/int:pk|PUT|Update|장바구니 상품 업데이트|
|api/cart-items/int:pk|PATCH|Partial_Update|장바구니 상품 세부내역 부분 업데이트|
|api/cart-items/int:pk|DELETE|Delete|장바구니 상품 삭제|




### orders


URL|Method|Action|Description|
|------|---|---|---|
|api/orders|GET|List|주문서 전체 목록 조회|
|api/orders|POST|Create|주문서 생성|
|api/orders/int:pk|GET|Retrieve|주문서 세부내역 조회|


* update,delete 불가


URL|Method|Description|
|------|---|---|
|api/orders/summary/v1|GET|요약(SQL)|
|api/orders/summary/v2|GET|요약 **웹페이지** (ORM)|

### products


URL|Method|Action|Description|
|------|---|---|---|
|api/products|GET|List|상품 전체 목록 조회|
|api/products|POST|Create|상품 생성|
|api/products/int:pk|GET|Retrieve|상품 세부내역 조회|
|api/products/int:pk|PUT|Update|상품 세부내역 업데이트|
|api/products/int:pk|PATCH|Partial_Update|상품 세부내역 부분 업데이트|
|api/products/int:pk|DELETE|Delete|상품 삭제|

</br>

- [API 명세서](https://documenter.getpostman.com/view/21842492/2s8YK4rSnc)



</br>


## TIL


- [[TIL] dj_rest_auth Custom 회원가입 만들기 (+ Custom model)](https://medium.com/@heeee/til-dj-rest-auth-custom-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EB%A7%8C%EB%93%A4%EA%B8%B0-custom-model-f1ad5a29f170)

- [[TIL] Django 모델에 choice 추가하기(default 옵션 잘 이용하기)](https://medium.com/@heeee/til-django-%EB%AA%A8%EB%8D%B8%EC%97%90-choice-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0-default-%EC%98%B5%EC%85%98-%EC%9E%98-%EC%9D%B4%EC%9A%A9%ED%95%98%EA%B8%B0-b18cfd8f4b16)

- [[TIL] Django raw SQL 쿼리 사용하기](https://medium.com/@heeee/til-django-raw-sql-%EC%BF%BC%EB%A6%AC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-ac427965ca79)








