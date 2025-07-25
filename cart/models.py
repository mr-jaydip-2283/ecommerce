from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
