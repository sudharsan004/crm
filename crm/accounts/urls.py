from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<int:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>/', views.deleteOrder, name="delete_order"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<int:pk>/',
         views.updateCustomer, name='update_customer'),
    path('create_customer_orders/<int:customer_id>/',
         views.createCustomerOrders, name="create_customer_orders"),


]
