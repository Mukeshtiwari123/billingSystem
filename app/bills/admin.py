from django.contrib import admin

from .models import Role,Charges,Bills,BillCharge,User,Receipt,ReceiptCharge,PaymentMode
# Register your models here.

admin.site.register(Role)
admin.site.register(Charges)
admin.site.register(Bills)
admin.site.register(BillCharge)
admin.site.register(User)
admin.site.register(Receipt)
admin.site.register(ReceiptCharge)
admin.site.register(PaymentMode)
