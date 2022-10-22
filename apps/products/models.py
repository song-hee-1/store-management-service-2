from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name="상품이름")
    description = models.TextField(verbose_name="상품설명")
    stock = models.PositiveIntegerField(verbose_name="재고")
    create_at = models.DateTimeField(auto_now=True, verbose_name="상품 업로드 날짜")

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = "상품 목록"
        db_table = 'product'

    def __str__(self):
        return self.name
