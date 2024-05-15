from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


