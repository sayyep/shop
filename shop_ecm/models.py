from django.db import models


class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    describe = models.CharField(max_length=2000)
    image = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'product'
