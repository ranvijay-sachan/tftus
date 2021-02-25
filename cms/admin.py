from django.contrib import admin
from .models import SalesMan, Customer, CustomerCallHistory


@admin.register(SalesMan)
class SalesManAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerCallHistory)
class CustomerCallHistoryAdmin(admin.ModelAdmin):
    pass
