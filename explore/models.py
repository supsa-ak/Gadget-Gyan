from django.db import models


# Create your models here.
class Product(models.Model):
    device_id = models.AutoField
    product_name = models.CharField(max_length=50)
    display = models.CharField(max_length=50, default="")
    processor = models.CharField(max_length=50, default="")
    frontcam = models.CharField(max_length=50, default="")
    rearcam = models.CharField(max_length=50, default="")
    batterycap = models.CharField(max_length=50, default="")
    imglink = models.CharField(max_length=300, default="")
    price = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="explore/images", default="")

    def __str__(self):
        return self.product_name