from django.db import models
from django.core.validators import RegexValidator


class Order(models.Model):
    ORDER_STATE_CHOICES = (
        ('결제취소', 0),
        ('결제완료', 1),
    )

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, db_column='user_id',
                             related_name='order')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, db_column='product_id',
                                related_name='order_product')
    address = models.CharField(max_length=255, verbose_name="주소")
    receiver_name = models.CharField(max_length=40, verbose_name="수령자이름")
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    receiver_phone_number = models.CharField(validators=[phoneNumberRegex], max_length=13,
                                             help_text="휴대폰 번호는 다음과 같은 형식을 따라야 합니다: 010-1234-5678")
    order_state = models.CharField(max_length=4, default=1, choices=ORDER_STATE_CHOICES, verbose_name="주문서 상태")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="주문 날짜")
    total_price = models.PositiveIntegerField(null=True, verbose_name="주문서 총 가격")

    class Meta:
        verbose_name = "주문"
        verbose_name_plural = "주문 목록"
        db_table = 'order'

    def __str__(self):
        return str(self.id)
