from django.db import models


class Data(models.Model):
    ex_id = models.PositiveSmallIntegerField(db_index=True, primary_key=True)
    order_id = models.CharField(db_index=True, max_length=10)
    price_usd = models.DecimalField(max_digits=9, decimal_places=2)
    delivery_date = models.DateField(null=None, max_length=12)
    price_uah = models.DecimalField(max_digits=9, decimal_places=2)
    massage_to_telegram = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ex_id} - {self.price_usd}"
