from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=250, null=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    phone = PhoneNumberField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery')
    ]
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ManyToManyField(Product, null=True)
    status = models.CharField(null=True, max_length=150, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer.name + "'s order"
