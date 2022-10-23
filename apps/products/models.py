from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name="상품 이름")
    description = models.TextField(verbose_name="상품 설명")
    price = models.PositiveIntegerField(verbose_name="상품 가격", default=0)
    stock = models.PositiveIntegerField(verbose_name="재고")
    create_at = models.DateTimeField(auto_now=True, verbose_name="상품 업로드 날짜")
    order = models.ManyToManyField(
        "accounts.User",
        through="orders.Order",
        related_name='user_order',
        blank=True,
        verbose_name="상품 주문내역"
    )

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = "상품 목록"
        db_table = 'product'

    def __str__(self):
        return self.name
