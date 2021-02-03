from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.oder import Oder


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'description', 'image', 'category_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'password']


class OderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'price',
                    'address', 'phone', 'date', 'status', 'customer_id', 'product_id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Oder, OderAdmin)
