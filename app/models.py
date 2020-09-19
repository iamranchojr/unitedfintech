from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=14, decimal_places=2)

