from django.db import models

from eshopping_app.models import products_db


class e_cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'e_cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class e_cart_item(models.Model):
    product = models.ForeignKey(products_db, on_delete=models.CASCADE)
    cart = models.ForeignKey(e_cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'e_cart_item'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)