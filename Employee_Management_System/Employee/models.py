from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_Id  = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    designation = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
