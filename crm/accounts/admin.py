from django.contrib import admin

from .models import Category, Customer, Product, Order

admin.site.register([Category, Customer, Product, Order])
