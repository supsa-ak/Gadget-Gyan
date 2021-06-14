from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    image_link = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name