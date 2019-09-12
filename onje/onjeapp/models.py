from django.db import models

# Create your models here.


class customer (models.Model):
    name = models.CharField("Full name", max_length=500,)
    address1 = models.CharField("Address line1", max_length=500)
    address2 = models.CharField("Address line2", max_length=500)
    zip_code = models.CharField("ZIP/ Postal Code", max_length=10)
    city = models.CharField("City", max_length=50)

    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField("Full name", max_length=500,)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default = 12.99)
    zip_code = models.CharField("ZIP/ Postal Code", max_length=10)
    city = models.CharField("City", max_length=50)

    def __str__(self):
        return self.name
