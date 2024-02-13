from django.contrib import admin

from .models import Charges,Bills,BillCharge,Receipt,ReceiptCharge,PaymentMode
# Register your models here.


admin.site.register(Charges)
admin.site.register(Bills)
admin.site.register(BillCharge)
admin.site.register(Receipt)
admin.site.register(ReceiptCharge)
admin.site.register(PaymentMode)
