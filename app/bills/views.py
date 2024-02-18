from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from .models import Charges
from .forms import ChargesForm

from .models import Bills
from .forms import BillsForm

from .models import BillCharge
from .forms import BillChargeForm

from .models import Receipt
from .forms import ReceiptForm

from .models import ReceiptCharge
from .forms import ReceiptChargeForm

from .models import PaymentMode
from .forms import PaymentModeForm



from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my site!")


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.forms import ModelForm
from django import forms

class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})














# Create your views
from django.shortcuts import render  
from bills.forms import StudentForm  

def example_view(request):
    return render(request, 'example.html')

def index(request):  
    student = StudentForm()  
    return render(request,"index.html",{'form':student})



# Create view
def charge_create(request):
    if request.method == 'POST':
        form = ChargesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('charge_list')  # Redirect to the view displaying all charges
    else:
        form = ChargesForm()
    return render(request, 'charges/charge_form.html', {'form': form})

# Read/List view
def charge_list(request):
    charges = Charges.objects.all()
    return render(request, 'charges/charge_list.html', {'charges': charges})

# Update view
def charge_update(request, pk):
    charge = get_object_or_404(Charges, pk=pk)
    if request.method == 'POST':
        form = ChargesForm(request.POST, instance=charge)
        if form.is_valid():
            form.save()
            return redirect('charge_list')
    else:
        form = ChargesForm(instance=charge)
    return render(request, 'charges/charge_form.html', {'form': form})

# Delete view
def charge_delete(request, pk):
    charge = get_object_or_404(Charges, pk=pk)
    if request.method == 'POST':
        charge.delete()
        return redirect('charge_list')
    return render(request, 'charges/charge_confirm_delete.html', {'object': charge})




# Create view
def bill_create(request):
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillsForm()
    return render(request, 'bills/bill_form.html', {'form': form})

# Read/List view
def bill_list(request):
    bills = Bills.objects.all()
    return render(request, 'bills/bill_list.html', {'bills': bills})

# Update view
def bill_update(request, pk):
    bill = get_object_or_404(Bills, pk=pk)
    if request.method == 'POST':
        form = BillsForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillsForm(instance=bill)
    return render(request, 'bills/bill_form.html', {'form': form})

# Delete view
def bill_delete(request, pk):
    bill = get_object_or_404(Bills, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'bills/bill_confirm_delete.html', {'object': bill})



# Create view
def bill_charge_create(request):
    if request.method == 'POST':
        form = BillChargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_charge_list')
    else:
        form = BillChargeForm()
    return render(request, 'bill_charge/bill_charge_form.html', {'form': form})

# Read/List view
def bill_charge_list(request):
    bill_charges = BillCharge.objects.all()
    return render(request, 'bill_charge/bill_charge_list.html', {'bill_charges': bill_charges})

# Update view
def bill_charge_update(request, pk):
    bill_charge = get_object_or_404(BillCharge, pk=pk)
    if request.method == 'POST':
        form = BillChargeForm(request.POST, instance=bill_charge)
        if form.is_valid():
            form.save()
            return redirect('bill_charge_list')
    else:
        form = BillChargeForm(instance=bill_charge)
    return render(request, 'bill_charge/bill_charge_form.html', {'form': form})

# Delete view
def bill_charge_delete(request, pk):
    bill_charge = get_object_or_404(BillCharge, pk=pk)
    if request.method == 'POST':
        bill_charge.delete()
        return redirect('bill_charge_list')
    return render(request, 'bill_charge/bill_charge_confirm_delete.html', {'object': bill_charge})



# Create view
def receipt_create(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipt_list')
    else:
        form = ReceiptForm()
    return render(request, 'receipts/receipt_form.html', {'form': form})

# Read/List view
def receipt_list(request):
    receipts = Receipt.objects.all()
    return render(request, 'receipts/receipt_list.html', {'receipts': receipts})

# Update view
def receipt_update(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('receipt_list')
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'receipts/receipt_form.html', {'form': form})

# Delete view
def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        receipt.delete()
        return redirect('receipt_list')
    return render(request, 'receipts/receipt_confirm_delete.html', {'object': receipt})




# Create view
def receipt_charge_create(request):
    if request.method == 'POST':
        form = ReceiptChargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipt_charge_list')
    else:
        form = ReceiptChargeForm()
    return render(request, 'receipt_charge/receipt_charge_form.html', {'form': form})

# List view
def receipt_charge_list(request):
    receipt_charges = ReceiptCharge.objects.all()
    return render(request, 'receipt_charge/receipt_charge_list.html', {'receipt_charges': receipt_charges})

# Update view
def receipt_charge_update(request, pk):
    receipt_charge = get_object_or_404(ReceiptCharge, pk=pk)
    if request.method == 'POST':
        form = ReceiptChargeForm(request.POST, instance=receipt_charge)
        if form.is_valid():
            form.save()
            return redirect('receipt_charge_list')
    else:
        form = ReceiptChargeForm(instance=receipt_charge)
    return render(request, 'receipt_charge/receipt_charge_form.html', {'form': form})

# Delete view
def receipt_charge_delete(request, pk):
    receipt_charge = get_object_or_404(ReceiptCharge, pk=pk)
    if request.method == 'POST':
        receipt_charge.delete()
        return redirect('receipt_charge_list')
    return render(request, 'receipt_charge/receipt_charge_confirm_delete.html', {'object': receipt_charge})



def payment_mode_list(request):
    payment_modes = PaymentMode.objects.all()
    return render(request, 'payment_mode_list.html', {'payment_modes': payment_modes})

def payment_mode_create(request):
    if request.method == "POST":
        form = PaymentModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_mode_list')
    else:
        form = PaymentModeForm()
    return render(request, 'payment_mode_form.html', {'form': form})

def payment_mode_update(request, pk):
    payment_mode = get_object_or_404(PaymentMode, pk=pk)
    if request.method == "POST":
        form = PaymentModeForm(request.POST, instance=payment_mode)
        if form.is_valid():
            form.save()
            return redirect('payment_mode_list')
    else:
        form = PaymentModeForm(instance=payment_mode)
    return render(request, 'payment_mode_form.html', {'form': form})

def payment_mode_delete(request, pk):
    payment_mode = get_object_or_404(PaymentMode, pk=pk)
    if request.method == "POST":
        payment_mode.delete()
        return redirect('payment_mode_list')
    return render(request, 'payment_mode_confirm_delete.html', {'payment_mode': payment_mode})


# app/views.py
from django.http import HttpResponse
from .models import Bills, Receipt
from .utils import render_to_pdf

def bill_pdf_view(request, pk):
    try:
        bill = Bills.objects.get(pk=pk)
        context = {'bill': bill}
        return render_to_pdf('bills/pdf_template.html', context)
    except Bills.DoesNotExist:
        return HttpResponse("Bill not found.", status=404)

def receipt_pdf_view(request, pk):
    try:
        receipt = Receipt.objects.get(pk=pk)
        context = {'receipt': receipt}
        return render_to_pdf('receipts/pdf_template.html', context)
    except Receipt.DoesNotExist:
        return HttpResponse("Receipt not found.", status=404)

