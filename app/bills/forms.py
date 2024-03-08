
from django import forms
import json
from django.forms import ModelForm, Textarea

from .models import Charges
from .models import Bills
from .models import BillCharge
from .models import Receipt
from .models import ReceiptCharge
from .models import PaymentMode


class JSONField(forms.CharField):
    def to_python(self, value):
        if not value:
            return []
        try:
            return json.loads(value)
        except ValueError:
            raise forms.ValidationError("Invalid JSON format")

    def prepare_value(self, value):
        if isinstance(value, str):
            return value
        return json.dumps(value)


class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)



class ChargesForm(forms.ModelForm):
    class Meta:
        model = Charges
        fields = ['charge_title', 'charge_percentage', 'charge_fixed_rate']


# To handle CRUD operations for the Bills model, similar steps to those for the Charges model are followed. 
# You'll need a form for the Bills model and views to create, read, update, and delete instances of Bills
# class BillsForm(forms.ModelForm):
#     class Meta:
#         model = Bills
#         fields = ['bil_customer', 'bil_type', 'bil_description', 'bil_number', 'bil_receipt_date', 'bil_charges','bil_items']
#         widgets = {
#             'bil_receipt_date': forms.DateInput(attrs={'type': 'date'}),
#             'bil_charges': forms.CheckboxSelectMultiple,
#             # 'bil_items': forms.CheckboxSelectMultiple,
#         }
class BillsForm(ModelForm):
    bil_items = JSONField(widget=Textarea(attrs={'id': 'bil_items_json'}), required=False)

    class Meta:
        model = Bills
        fields = ['bil_customer', 'bil_type', 'bil_description', 'bil_number', 'bil_receipt_date', 'bil_charges', 'bil_items']
        widgets = {
                'bil_receipt_date': forms.DateInput(attrs={'type': 'date'}),
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

# Form creation for getting the requirement for sending the email.

class EmailPDFForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = forms.EmailField(label="Recipient's Email")
