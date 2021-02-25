from rest_framework import viewsets
from .models import SalesMan, Customer, CustomerCallHistory
from .serializers import SalesManSerializers, CustomerSerializers


class SalesManViewSet(viewsets.ModelViewSet):
    """
    list:
    This API returns a list of all the existing SalesMan.

    create:
    This API is used to create a new SalesMan.

    retrieve:
    This API retrieves an existing SalesMan for a given ID.

    update:
    This API updates an existing SalesMan for a given ID.

    patch:
    partially update a existing SalesMan instance.

    destroy:
    This API deletes an existing SalesMan for a given ID.
    """
    queryset = SalesMan.objects.all().order_by('-id')
    serializer_class = SalesManSerializers


class CustomerViewSet(viewsets.ModelViewSet):
    """
    list:
    This API returns a list of all the existing Customer.

    create:
    This API is used to create a new Customer.

    retrieve:
    This API retrieves an existing Customer for a given ID.

    update:
    This API updates an existing Customer for a given ID.

    patch:
    partially update a existing Customer instance.

    destroy:
    This API deletes an existing Customer for a given ID.
    """
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializers

