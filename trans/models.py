from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    
    def __str__(self):
        return self.alias

class Truck(models.Model):
    serial = models.IntegerField(unique=True)
    year = models.IntegerField()
    model = models.CharField(max_length=64)

    def __str__(self):
        return "{} {}".format(self.model, self.year)

class Freight(models.Model):
    origin = models.CharField(max_length=32)
    destiny = models.CharField(max_length=32)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, blank=False, null=True)
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, blank=False, null=True)
    start_time = models.DateField(max_length=32)
    end_time = models.DateField(max_length=32)    
    comment = models.TextField()

    def __str__(self):
        return "{}: {}-{}".format(self.id, self.origin, self.destiny)

class Discount(models.Model):
    DISCOUNT_STATUS = (
        ('p', 'PENDING'),
        ('d', 'PAID'),
        ('c', 'CANCELED'),
    )
    freight = models.ForeignKey(Freight, related_name='discounts', on_delete=models.CASCADE)
    _type = models.CharField(max_length=32)
    status = models.CharField(choices=DISCOUNT_STATUS, max_length=16)
    comments = models.TextField()

    def __str__(self):
        return "{}".format(self._type)


class Expense(models.Model):
    EXPENSE_STATUS = (
        ('p', 'PENDING'),
        ('d', 'PAID'),
        ('c', 'CANCELED'),
    )
    freight = models.ForeignKey(Freight, related_name='expenses', on_delete=models.CASCADE)
    product = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(choices=EXPENSE_STATUS, max_length=16)
    comment = models.CharField(max_length=128)

    def __str__(self):
        return "{}: ${}".format(self.product, self.cost * self.quantity)