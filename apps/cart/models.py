from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="cart", null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "장바구니"
        verbose_name_plural = "장바구니 목록"
        db_table = 'cart'

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, related_name="items", null=True)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, null=True,
                                related_name='cartitems')
    quantity = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "장바구니 상품"
        verbose_name_plural = "장바구니 상품 목록"
        db_table = 'cartitem'

    def __str__(self):
        return str(self.cart)
