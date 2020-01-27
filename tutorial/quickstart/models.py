from django.db import models


class Invoice(models.Model):
    date = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    big = models.IntegerField(default=0)
