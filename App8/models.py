from django.db import models


class ProductModel(models.Model):
    pno = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=32, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.pname
