from django.db import models
from store.models.product import Product
from store.models.customer import Customer
import datetime


class Oder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def place_oder(self):
        return self.save()

    @classmethod
    def get_all_product_by_customer_id(cls, customer_id):
        return cls.objects.filter(customer_id=customer_id)
