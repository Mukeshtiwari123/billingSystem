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
import json
import ast
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum, Case, When, F, DecimalField
from decimal import Decimal


# class Charges(models.Model):
#     charge_title = models.CharField(max_length=255)
#     charge_percentage = models.DecimalField(max_digits=100000, decimal_places=2, default=1)
#     charge_fixed_rate = models.DecimalField(max_digits=100000, decimal_places=2, default=1)

#     def __str__(self):
#         return self.charge_title

class Charges(models.Model):
    CHARGE_TYPE_CHOICES = (
        ('fixed', 'Fixed Rate'),
        ('percentage', 'Percentage'),
    )

    charge_title = models.CharField(max_length=255)
    charge_percentage = models.DecimalField(max_digits=100000, decimal_places=2, default=1)
    charge_fixed_rate = models.DecimalField(max_digits=100000, decimal_places=2, default=1)
    charge_type = models.CharField(max_length=10, choices=CHARGE_TYPE_CHOICES, default='fixed')

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

# class Bills(models.Model):
#     bil_customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     bil_type = models.CharField(max_length=255)
#     bil_description = models.TextField()
#     bil_number = models.CharField(max_length=255)
#     bil_receipt_date = models.DateField()
#     bil_charges = models.ManyToManyField('Charges', through='BillCharge')
#     # bil_items = models.ManyToManyField('Item', through='BillItem')
#     bil_items = models.TextField()  # Assuming this stores JSON data
    
#     def __str__(self):
#         return f"{self.pk} - {self.bil_type} - {self.bil_number}"

#     def set_items(self, items_list):
#         """
#         Stores a list of items (dicts) as a JSON string in bil_items.
#         """
#         self.bil_items = json.dumps(items_list, cls=DjangoJSONEncoder)

#     def get_items(self):
#         """
#         Retrieves the list of items stored in bil_items.
#         """
#         if self.bil_items:
#             return json.loads(self.bil_items)
#         return []
    
#     def calculate_total_with_charges(self):
#         """
#         Calculates the total amount for the bill, including all charges.
#         """
#         # Load the item costs from bil_items JSON field
#         items = self.get_items()
#         total_item_cost = sum(item['total_cost'] for item in items)
        
#         # Calculate charges from BillCharge
#         # Assuming BillCharge.amount for 'fixed' is an absolute value and for 'percentage' is a percent of total_item_cost
#         charges = self.billcharge_set.aggregate(
#             total_charges=Sum(
#                 Case(
#                     When(charge_type='fixed', then='amount'),
#                     When(charge_type='percentage', then=F('amount') / 100 * total_item_cost),
#                     output_field=DecimalField()
#                 )
#             )
#         )['total_charges'] or 0
        
#         # Calculate total including charges
#         total_with_charges = total_item_cost + charges
        
#         return total_with_charges

class Bills(models.Model):
    bil_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bil_type = models.CharField(max_length=255)
    bil_description = models.TextField()
    bil_number = models.CharField(max_length=255)
    bil_receipt_date = models.DateField()
    bil_charges = models.ManyToManyField('Charges', through='BillCharge')
    bil_items = models.TextField()  # Assuming this stores JSON data
    bil_total_with_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.pk} - {self.bil_type} - {self.bil_number}"

    def set_items(self, items_list):
        self.bil_items = json.dumps(items_list, cls=DjangoJSONEncoder)

    def get_items(self):
        if self.bil_items:
            print("------------->",self.bil_items)
            # return json.loads(self.bil_items)
            python_object = ast.literal_eval(self.bil_items)
            # Convert the Python object back to a string with JSON formatting
            json_string = json.dumps(python_object)
            return json.loads(json_string)
        return []

    # def calculate_total_with_charges(self):
    #     items = self.get_items()
    #     total_item_cost = sum(item['total_cost'] for item in items)
        
    #     charges = self.billcharge_set.aggregate(
    #         total_charges=Sum(
    #             Case(
    #                 When(charge_type='fixed', then='amount'),
    #                 When(charge_type='percentage', then=F('amount') / 100 * total_item_cost),
    #                 output_field=DecimalField()
    #             )
    #         )
    #     )['total_charges'] or 0
        
    #     total_with_charges = total_item_cost + charges
    #     print("total_with_charges---->",total_with_charges)
    #     print("charges---->",charges)
    #     return total_with_charges

    def calculate_total_with_charges(self):
        items = self.get_items()
        total_item_cost = sum(item['total_cost'] for item in items)
        charges = Decimal(0)  # Initialize total charges
        print("----------------------------------------------")
        # Iterate through each BillCharge related to this bill
        for bill_charge in self.billcharge_set.all():
            print("bill_charge---->",bill_charge)
            charge = bill_charge.charge
            print("charge.charge_type--->",charge.charge_type)
            if charge.charge_type == 'fixed':
                # If the charge is fixed, add its fixed rate to the total charges
                print("charge.charge_fixed_rate--->",charge.charge_fixed_rate)
                charges += charge.charge_fixed_rate
                print("total_with_charge---->", charges)
            elif charge.charge_type == 'percentage':
                # If the charge is percentage-based, calculate the percentage of the current total
                # and add it to the total charges
                print("charge.charge_percentage--->",charge.charge_percentage)
                percentage_amount = (charge.charge_percentage / Decimal(100)) * total_item_cost
                charges += percentage_amount
                print("total_with_charge---->", charges)
            print("==============================")
        print("----------------------------------------------")
        # Calculate the total cost including charges
        total_with_charges = total_item_cost + charges
        print("total_with_charges---->", total_with_charges)
        print("charges---->", charges)
        return total_with_charges

    def save(self, *args, **kwargs):
        self.bil_total_with_charges = self.calculate_total_with_charges()
        super(Bills, self).save(*args, **kwargs)


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



