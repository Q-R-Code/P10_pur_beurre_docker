from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(null=True)
    categories = models.CharField(max_length=500)
    nutriscore_grade = models.CharField(max_length=5, null=True)
    image_nutriments = models.URLField(max_length=1500)
    barcode = models.CharField(max_length=30)
    url = models.URLField(null=True)

    class Meta:
        verbose_name = "Product"
        ordering = ['nutriscore_grade']


class Sub_saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sub_saved"
