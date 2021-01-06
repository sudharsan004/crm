# generate filter(search form) similar as model forms

import django_filters
from django_filters import filters
from .models import *


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = '__all__'
