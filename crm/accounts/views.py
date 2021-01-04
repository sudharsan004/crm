from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from .forms import OrderForm


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


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'accounts/update_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'accounts/update_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order}
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    return render(request, 'accounts/delete.html', context)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    context = {'form': form}
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'accounts/update_form.html', context)
