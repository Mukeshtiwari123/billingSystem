from django.contrib import admin

# Register your models here.
from .models import BillItem,Customer,Bill
# Register your models here.
from .models import BillItem,Customer,Bill



# admin.site.register(Item)
# admin.site.register(Charges)
# admin.site.register(Bills)
admin.site.register(BillItem)
admin.site.register(Bill)
admin.site.register(Customer)
# admin.site.register(Receipt)
# admin.site.register(ReceiptCharge)
# admin.site.register(ReceiptItem)
# admin.site.register(PaymentMode)