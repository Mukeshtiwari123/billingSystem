from django.db import models

from django.conf import settings
from django.contrib.auth.models import User


# class Role(models.Model):
#     role_title = models.CharField(max_length=255)
#     role_description = models.TextField()

#     def __str__(self):
#         return self.role_title


# class Permission(models.Model):
#     per_role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     per_title = models.CharField(max_length=255)
#     per_description = models.TextField()

#     def __str__(self):
#         return self.per_title


class Charges(models.Model):
    charge_title = models.CharField(max_length=255)
    charge_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    charge_fixed_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.charge_title


class Bills(models.Model):
    bil_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bil_type = models.CharField(max_length=255)
    bil_description = models.TextField()
    bil_number = models.CharField(max_length=255)
    bil_receipt_date = models.DateField()

    # Linking to Charges model for GST, VAT, and other charges
    bil_charges = models.ManyToManyField(Charges, through='BillCharge')

    def __str__(self):
        return self.bil_number


class BillCharge(models.Model):
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
    charge = models.ForeignKey(Charges, on_delete=models.CASCADE)
    
    # New field to indicate whether the charge is a fixed rate or percentage for this specific charge
    charge_type = models.CharField(max_length=10, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')], default='percentage')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.bill} - {self.charge} - {self.amount}"


class User(models.Model):
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_dob = models.DateField()
    user_address = models.TextField()

    def __str__(self):
        return self.user_name


# class Receipt(models.Model):
#     receipt_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     receipt_type = models.CharField(max_length=255)
#     receipt_description = models.TextField()
#     receipt_number = models.IntegerField()
#     receipt_date = models.DateField()

#     # Linking to Charges model for GST, VAT, and other charges
#     receipt_charges = models.ManyToManyField(Charges, through='ReceiptCharge')

#     def __str__(self):
#         return f"{self.receipt_type} - {self.receipt_number}"


class Receipt(models.Model):
    receipt_user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_type = models.CharField(max_length=255)
    receipt_description = models.TextField()
    receipt_number = models.IntegerField()
    receipt_date = models.DateField()

    # Linking to Charges model for GST, VAT, and other charges
    receipt_charges = models.ManyToManyField(Charges, through='ReceiptCharge')

    def __str__(self):
        return f"{self.receipt_type} - {self.receipt_number}"


class ReceiptCharge(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    charge = models.ForeignKey(Charges, on_delete=models.CASCADE)

    # New field to indicate whether the charge is a fixed rate or percentage for this specific charge
    charge_type = models.CharField(max_length=10, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Rate')], default='percentage')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.receipt} - {self.charge} - {self.amount}"



class PaymentMode(models.Model):
    payment_mode_name = models.CharField(max_length=255)
    payment_mode_type_string = models.CharField(max_length=255)

    def __str__(self):
        return self.payment_mode_name

