from django.db import models


class SalesMan(models.Model):
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        app_label = 'cms'
        db_table = "salesman"

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True)
    added_date = models.DateTimeField(auto_now_add=True)
    my_free_time = models.DateTimeField()
    sales_man = models.ForeignKey(SalesMan, related_name="customer_salesman",
                                  on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'cms'
        db_table = "customer"

    def __str__(self):
        return self.name


class CustomerCallHistory(models.Model):
    call_start = models.DateTimeField()
    call_end = models.DateTimeField()
    note = models.TextField()
    customer_id = models.ForeignKey(Customer, related_name='call_history', on_delete=models.DO_NOTHING)
    sales_man = models.ForeignKey(SalesMan, related_name='attendee', on_delete=models.DO_NOTHING)
