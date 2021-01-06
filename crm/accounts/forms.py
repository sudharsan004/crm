from django.forms import ModelForm
from django import forms
from .models import *
from crispy_forms.layout import Layout, Div, Field


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
