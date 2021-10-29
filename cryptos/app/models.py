from django.db import models


class Order(models.Model):
    date = models.DateField(blank=False)
    item = models.CharField(max_length=210, blank=False)
    price = models.DecimalField(decimal_places=5, max_digits=21, default=0)
    quantity = models.DecimalField(decimal_places=5, max_digits=21, default=0)
    amount = models.DecimalField(decimal_places=5, max_digits=21, default=0)
   

    def __str__(self):
        return f"{self.date}: {self.item}"

