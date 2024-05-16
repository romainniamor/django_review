from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
