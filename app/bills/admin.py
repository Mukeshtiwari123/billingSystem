from django.contrib import admin

from .models import Charges,Bills,BillCharge,Receipt,ReceiptCharge,PaymentMode
# Register your models here.
from .models import Item,Charges,Bills,BillCharge,BillItem,Receipt,ReceiptCharge,ReceiptItem



admin.site.register(Item)
admin.site.register(Charges)
admin.site.register(Bills)
admin.site.register(BillCharge)
admin.site.register(BillItem)
admin.site.register(Receipt)
admin.site.register(ReceiptCharge)
admin.site.register(ReceiptItem)
admin.site.register(PaymentMode)
