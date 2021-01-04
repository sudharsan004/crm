from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    last_five_orders = Order.objects.filter().order_by('-id')[:5]
    last_five = reversed(last_five_orders)
    total_order_count = Order.objects.all().count()
    orders_delivered_count = Order.objects.filter(status="Delivered").count()
    orders_pending_count = total_order_count-orders_delivered_count
    customer = Customer.objects.all()

    context = {'orders': last_five, 'customers': customer,
               'order_stats': {'total_orders': total_order_count,
                               'orders_delivered': orders_delivered_count,
                               'orders_pending': orders_pending_count
                               }}
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    all_orders = customer.order_set.all()
    try:
        orders_delivered = customer.order_set.filter(
            status="Delivered").count()
    except Order.DoesNotExist:
        orders_delivered = 0
    try:
        orders_pending = customer.order_set.filter(status="Pending").count()
    except Order.DoesNotExist:
        orders_pending = 0
    orders_out_for_delivery = all_orders.count()-(orders_delivered+orders_pending)

    context = {'customer': customer, 'all_orders': all_orders,
               'orders_delivered': orders_delivered, 'orders_pending': orders_pending, 'orders_out_for_delivery': orders_out_for_delivery}
    return render(request, 'accounts/customer.html', context=context)


def order_view(request):
    
    return render(request,'accounts/order_form.html')
