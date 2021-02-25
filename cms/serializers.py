from rest_framework import serializers
from .models import SalesMan, Customer


class SalesManSerializers(serializers.ModelSerializer):

    class Meta:
        model = SalesMan
        fields = ['id', 'name']


class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'added_date', 'email', 'my_free_time', 'sales_man']

