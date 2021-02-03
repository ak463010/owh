from django.db import models
from .category import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/product', default=None)
    description = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

    @classmethod
    def get_all_product(cls):
        return cls.objects.all()

    @classmethod
    def get_product_by_category_id(cls, id):
        return cls.objects.filter(category_id=id)

    @classmethod
    def get_product_by_ids(cls, ids):
        return cls.objects.filter(id__in=ids)
