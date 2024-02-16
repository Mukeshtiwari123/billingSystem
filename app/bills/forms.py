

from django import forms 
from .models import Charges
from .models import Bills
from .models import BillCharge
from .models import Receipt
from .models import ReceiptCharge
from .models import PaymentMode





class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)



class ChargesForm(forms.ModelForm):
    class Meta:
        model = Charges
        fields = ['charge_title', 'charge_percentage', 'charge_fixed_rate']


# To handle CRUD operations for the Bills model, similar steps to those for the Charges model are followed. 
# You'll need a form for the Bills model and views to create, read, update, and delete instances of Bills
class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ['bil_customer', 'bil_type', 'bil_description', 'bil_number', 'bil_receipt_date', 'bil_charges']
        widgets = {
            'bil_receipt_date': forms.DateInput(attrs={'type': 'date'}),
            'bil_charges': forms.CheckboxSelectMultiple,
        }




class BillChargeForm(forms.ModelForm):
    class Meta:
        model = BillCharge
        fields = ['bill', 'charge', 'charge_type', 'amount']



class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['receipt_user', 'receipt_type', 'receipt_description', 'receipt_number', 'receipt_date', 'receipt_charges']



class ReceiptChargeForm(forms.ModelForm):
    class Meta:
        model = ReceiptCharge
        fields = ['receipt', 'charge', 'charge_type', 'amount']




class PaymentModeForm(forms.ModelForm):
    class Meta:
        model = PaymentMode
        fields = ['payment_mode_name', 'payment_mode_type_string']


class PaymentModeForm(forms.ModelForm):
    class Meta:
        model = PaymentMode
        fields = ['payment_mode_name', 'payment_mode_type_string']
