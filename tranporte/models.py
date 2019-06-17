from django.db import models


class Driver(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    alias = models.CharField()

class Truck(models.Model):
    serial = models.IntegerField(unique=True)
    year = models.IntegerField()
    model = models.CharField()


class Freight(models.Model):
    origin = models.CharField()
    destiny = models.CharField()
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, blank=False, null=True)
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, blank=False, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()    
    comment = models.CharField()


class Discount(models.Model):
    DISCOUNT_STATUS = (
        ('p', 'PENDING'),
        ('d', 'PAID'),
        ('c', 'CANCELED'),
    )
    freight = models.ForeignKey(Freight, related_name='discounts', on_delete=models.CASCADE)
    _type = models.CharField()
    status = models.CharField(choices=DISCOUNT_STATUS)
    comments = models.CharField()


class Expense(models.Model):
    EXPENSE_STATUS = (
        ('p', 'PENDING'),
        ('d', 'PAID'),
        ('c', 'CANCELED'),
    )
    freight = models.ForeignKey(Freight, related_name='expenses', on_delete=models.CASCADE)
    product = models.CharField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(choices=EXPENSE_STATUS)
    comment = models.CharField(max_length=128)
