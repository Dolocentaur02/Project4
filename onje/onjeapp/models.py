from django.db import models

# Create your models here.


class ShippingAddress (models.Model):
    name = models.CharField("Full name", max_length=500,)
    address1 = models.CharField("Address line2", max_length=500)
    address2 = models.CharField("Address line2", max_length=500)
    zip_code = models.CharField("ZIP/ Postal Code", max_length=10)
    city = models.CharField("City", max_length=50)

    def __str__(self):
        return self.name
