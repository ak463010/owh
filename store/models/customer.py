from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def register_user(self):
        return self.save()

    def is_exist(self):
        try:
            if Customer.objects.get(email=self.email):
                return True
            return False
        except:
            return None

    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return None
