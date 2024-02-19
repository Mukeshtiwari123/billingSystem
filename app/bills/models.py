# from django.db import models
# from django.contrib.auth.models import User
# from django import forms

# class Charges(models.Model):
#     charge_title = models.CharField(max_length=255)
#     charge_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     charge_fixed_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return self.charge_title

# class Bills(models.Model):
#     bil_customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     bil_type = models.CharField(max_length=255)
#     bil_description = models.TextField()
#     bil_number = models.CharField(max_length=255)
#     bil_receipt_date = models.DateField()
#     bil_charges = models.ManyToManyField(Charges, through='BillCharge')

#     def __str__(self):
#         return self.bil_number

# class BillCharge(models.Model):
#     bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
#     charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
#     charge_type = models.CharField(
#         max_length=10,
#         choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')],
#         default='percentage'
#     )
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return f"{self.bill} - {self.charge} - {self.amount}"

# class Receipt(models.Model):
#     receipt_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     receipt_type = models.CharField(max_length=255)
#     receipt_description = models.TextField()
#     receipt_number = models.IntegerField()
#     receipt_date = models.DateField()
#     receipt_charges = models.ManyToManyField(Charges, through='ReceiptCharge')

#     def __str__(self):
#         return f"{self.receipt_type} - {self.receipt_number}"

# class ReceiptCharge(models.Model):
#     receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
#     charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
#     charge_type = models.CharField(
#         max_length=10,
#         choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')],
#         default='percentage'
#     )
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return f"{self.receipt} - {self.charge} - {self.amount}"

# class PaymentMode(models.Model):
#     payment_mode_name = models.CharField(max_length=255)
#     payment_mode_type_string = models.CharField(max_length=255)

#     def __str__(self):
#         return self.payment_mode_name

# # Form example remains unchanged, as it is not directly related to the Django model adjustments
# class StudentForm(forms.Form):  
#     firstname = forms.CharField(label="Enter first name", max_length=50)  
#     lastname  = forms.CharField(label="Enter last name", max_length=100)



# from django.db import models
# from django.contrib.auth.models import User

# class Item(models.Model):
#     item_name = models.CharField(max_length=255)
#     item_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.item_name

# class Charges(models.Model):
#     charge_title = models.CharField(max_length=255)
#     charge_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     charge_fixed_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return self.charge_title

# class Bills(models.Model):
#     bil_customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     bil_type = models.CharField(max_length=255)
#     bil_description = models.TextField()
#     bil_number = models.CharField(max_length=255)
#     bil_receipt_date = models.DateField()
#     bil_charges = models.ManyToManyField(Charges, through='BillCharge')
#     bil_items = models.ManyToManyField(Item, through='BillItem')  # Link to items

#     def __str__(self):
#         return self.bil_number

# class BillCharge(models.Model):
#     bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
#     charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
#     charge_type = models.CharField(
#         max_length=10,
#         choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')],
#         default='percentage'
#     )
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return f"{self.bill} - {self.charge} - {self.amount}"

# class BillItem(models.Model):  # New model for linking items to bills
#     bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.item} x {self.quantity} in {self.bill}"

# class Receipt(models.Model):
#     receipt_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     receipt_type = models.CharField(max_length=255)
#     receipt_description = models.TextField()
#     receipt_number = models.IntegerField()
#     receipt_date = models.DateField()
#     receipt_charges = models.ManyToManyField(Charges, through='ReceiptCharge')
#     receipt_items = models.ManyToManyField(Item, through='ReceiptItem')  # Link to items

#     def __str__(self):
#         return f"{self.receipt_type} - {self.receipt_number}"

# # Similar to BillItem, create a ReceiptItem model for linking items to receipts

# class ReceiptCharge(models.Model):
#     receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
#     charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
#     charge_type = models.CharField(
#         max_length=10,
#         choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')],
#         default='percentage'
#     )
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return f"{this.receipt} - {this.charge} - {this.amount}"

# class ReceiptItem(models.Model):  # New model for linking items to receipts
#     receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{this.item} x {this.quantity} in {this.receipt}"

# class PaymentMode(models.Model):
#     payment_mode_name = models.CharField(max_length=255)
#     payment_mode_type_string = models.CharField(max_length=255)

#     def __str__(self):
#         return self.payment_mode_name

# # Form example remains unchanged, as it is not directly related to the Django model adjustments
# class StudentForm(forms.Form):  
#     firstname = forms.CharField(label="Enter first name", max_length=50)  
#     lastname  = forms.CharField(label="Enter last name", max_length=100)
















from django.db import models
from django.contrib.auth.models import User
from django import forms

class Charges(models.Model):
    charge_title = models.CharField(max_length=255)
    charge_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    charge_fixed_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.charge_title

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True)

    def __str__(self):
        return self.item_name

class BillItem(models.Model):
    bill = models.ForeignKey('Bills', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item.item_name} x {self.quantity} - {self.bill.bil_number}"

class Bills(models.Model):
    bil_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bil_type = models.CharField(max_length=255)
    bil_description = models.TextField()
    bil_number = models.CharField(max_length=255)
    bil_receipt_date = models.DateField()
    bil_charges = models.ManyToManyField('Charges', through='BillCharge')
    bil_items = models.ManyToManyField('Item', through='BillItem')

    def __str__(self):
        return f"{self.pk} - {self.bil_type} - {self.bil_number}"


class BillCharge(models.Model):
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
    charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
    charge_type = models.CharField(
        max_length=10,
        choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')],
        default='percentage'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.bill} - {self.charge} - {self.amount}"

class ReceiptItem(models.Model):
    receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item.item_name} x {self.quantity} - {self.receipt.receipt_number}"

class Receipt(models.Model):
    receipt_user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_type = models.CharField(max_length=255)
    receipt_description = models.TextField()
    receipt_number = models.IntegerField()
    receipt_date = models.DateField()
    receipt_charges = models.ManyToManyField('Charges', through='ReceiptCharge')
    receipt_items = models.ManyToManyField('Item', through='ReceiptItem')

    def __str__(self):
        return f"{self.pk} - {self.receipt_type} - {self.receipt_number}"

class ReceiptCharge(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
    charge_type = models.CharField(
        max_length=10,
        choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')],
        default='percentage'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.receipt} - {self.charge} - {self.amount}"

class PaymentMode(models.Model):
    payment_mode_name = models.CharField(max_length=255)
    payment_mode_type_string = models.CharField(max_length=255)

    def __str__(self):
        return self.payment_mode_name

# Form example remains unchanged, as it is not directly related to the Django model adjustments
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name", max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length=100)



