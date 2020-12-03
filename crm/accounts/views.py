from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    last_five_orders = Order.objects.filter().order_by('-id')[:5]
    last_five = reversed(last_five_orders)
    orders = Order.objects.all()
    customer = Customer.objects.all()
    context = {'orders': last_five, 'customers': customer}
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()

    return render(request, 'accounts/product.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')
