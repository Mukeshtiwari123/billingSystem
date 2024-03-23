from django.contrib import admin

from .models import *
# Register your models here.



admin.site.register(Item)
admin.site.register(Charges)
admin.site.register(Bills)
admin.site.register(BillCharge)
admin.site.register(BillItem)
admin.site.register(Receipt)
admin.site.register(ReceiptCharge)
admin.site.register(ReceiptItem)
admin.site.register(PaymentMode)
admin.site.register(Profile)

