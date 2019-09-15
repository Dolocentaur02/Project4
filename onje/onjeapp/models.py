from django.db import models

# Create your models here.


class Contact (models.Model):
    name = models.CharField(default=" ", max_length=500,)
    address1 = models.CharField(default="Address line1", max_length=500)
    address2 = models.CharField(default="Address line2", max_length=500)
    zip_code = models.CharField(default="ZIP/ Postal Code", max_length=10)
    city = models.CharField(default="City", max_length=50)

    def __str__(self):
        return self.name


class Product (models.Model):
    title = models.CharField(default=" ", max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=15.99)
    image_url = models.CharField(default='', max_length=512)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    name = models.CharField(default=" ", max_length=500,)
    Products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(
        default=0.00, max_digits=20, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return str(self.name)
