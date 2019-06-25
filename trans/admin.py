from django.contrib import admin
from .models import Driver, Truck, Freight, Discount, Expense

class ExpensesInline(admin.TabularInline):
    model = Expense


# Register your models here.
admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Freight, inlines=[ExpensesInline])
admin.site.register(Discount)
admin.site.register(Expense)