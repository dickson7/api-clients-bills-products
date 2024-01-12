from django.db import models

class Client(models.Model):
    document = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=20)
    code = models.CharField(max_length=20)

class BillProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)