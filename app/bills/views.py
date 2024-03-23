from django.shortcuts import render

from django.contrib.auth.decorators import login_required


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

import json


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my site!")


from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.forms import ModelForm
from django import forms
import re

from django.core.exceptions import ValidationError


class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password','password2',)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        if password:
            # Check for at least one lowercase letter
            if not re.search('[a-z]', password):
                raise ValidationError('The password must contain at least one lowercase letter.')
            # Check for at least one uppercase letter
            if not re.search('[A-Z]', password):
                raise ValidationError('The password must contain at least one uppercase letter.')
            # Check for at least one special character
            if not re.search('[^A-Za-z0-9]', password):
                raise ValidationError('The password must contain at least one special character.')
        # Ensure you also return the cleaned data
        return password





# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         print("indrester")
#         print(form.is_valid())
#         print(UserRegistrationForm)
#           # Print all key-value pairs from the POST data
#         for key, value in request.POST.items():
#             print(f"{key}: {value}")
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             # Authenticate and login are optional here, depending on whether you want to log the user in directly after registration
#             user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
#             login(request, user)
#             # Redirect to login page after successful registration
#             return redirect('login')  # Use the name of your login route
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib import messages
# from .forms import UserRegistrationForm  # Ensure you have the correct import path

def register(request):
    message = ""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Instantiate form with POST data
        if form.is_valid():
            print(  form.cleaned_data['username'],
                    form.cleaned_data['first_name'],
                    form.cleaned_data['last_name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'])
            # Process the form data, e.g., create a user
            User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            message = 'Registration successful. You can now log in.'
            # Redirect to a new URL, for example, the login page
            return redirect('/bills')  # Change 'login_url_name' to your login view's URL name
        else:
            message = "Invalid username or password." 
            messages.error(request, "Invalid username or password.")
    else:
        form = UserRegistrationForm()  # Instantiate an empty form for GET request

    return render(request, 'register.html', {'form': form, 'message': message})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def user_login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password2")
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You are now logged in.")
            return redirect("/bills")  # Redirect to a home or dashboard page
        else:
            message = "Invalid username or password." 
            messages.error(request, "Invalid username or password.")
            
    return render(request, "login.html", {'message': message})  # Path to your login template


def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect back to the login page



@login_required
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
@login_required
# Read/List view
def charge_list(request):
    charges = Charges.objects.all()
    return render(request, 'charges/charge_list.html', {'charges': charges})

@login_required
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
@login_required
# Delete view
def charge_delete(request, pk):
    charge = get_object_or_404(Charges, pk=pk)
    if request.method == 'POST':
        charge.delete()
        return redirect('charge_list')
    return render(request, 'charges/charge_confirm_delete.html', {'object': charge})



@login_required
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

# @login_required
# # Create view
# def bill_create(request, bill_id=None):
#     bill = None
#     if bill_id:
#         bill = get_object_or_404(Bills, pk=bill_id)

#     if request.method == 'POST':
#         form = BillsForm(request.POST, instance=bill)
#         items = [value for key, value in request.POST.items() if key.startswith('item_')]
#         # You might want to validate items here
#         if form.is_valid():
#             bill = form.save(commit=False)
#             bill.bil_items = json.dumps(items)  # Assuming items should be stored as a JSON list
#             bill.save()
#             return redirect('bill_list')  # Replace with your actual view name
#     else:
#         form = BillsForm(instance=bill)
#         items = []

#     if bill and bill.bil_items:
#         items = json.loads(bill.bil_items)

#     return render(request, 'bills/bill_form.html', {
#         'form': form,
#         'items': items,  # Pass items to the template to prepopulate if editing
#     })

@login_required
# Read/List view
def bill_list(request):
    bills = Bills.objects.all()
    return render(request, 'bills/bill_list.html', {'bills': bills})
@login_required
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
@login_required
# Delete view
def bill_delete(request, pk):
    bill = get_object_or_404(Bills, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'bills/bill_confirm_delete.html', {'object': bill})

@login_required
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

@login_required
# Read/List view
def bill_charge_list(request):
    bill_charges = BillCharge.objects.all()
    return render(request, 'bill_charge/bill_charge_list.html', {'bill_charges': bill_charges})

@login_required
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

@login_required
# Delete view
def bill_charge_delete(request, pk):
    bill_charge = get_object_or_404(BillCharge, pk=pk)
    if request.method == 'POST':
        bill_charge.delete()
        return redirect('bill_charge_list')
    return render(request, 'bill_charge/bill_charge_confirm_delete.html', {'object': bill_charge})


@login_required
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

@login_required
# Read/List view
def receipt_list(request):
    receipts = Receipt.objects.all()
    return render(request, 'receipts/receipt_list.html', {'receipts': receipts})

@login_required
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

@login_required
# Delete view
def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        receipt.delete()
        return redirect('receipt_list')
    return render(request, 'receipts/receipt_confirm_delete.html', {'object': receipt})



@login_required
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
@login_required
# List view
def receipt_charge_list(request):
    receipt_charges = ReceiptCharge.objects.all()
    return render(request, 'receipt_charge/receipt_charge_list.html', {'receipt_charges': receipt_charges})
@login_required
# @Update view
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

@login_required
# Delete view
def receipt_charge_delete(request, pk):
    receipt_charge = get_object_or_404(ReceiptCharge, pk=pk)
    if request.method == 'POST':
        receipt_charge.delete()
        return redirect('receipt_charge_list')
    return render(request, 'receipt_charge/receipt_charge_confirm_delete.html', {'object': receipt_charge})

@login_required
def payment_mode_list(request):
    payment_modes = PaymentMode.objects.all()
    return render(request, 'payment_mode_list.html', {'payment_modes': payment_modes})

@login_required
def payment_mode_create(request):
    if request.method == "POST":
        form = PaymentModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_mode_list')
    else:
        form = PaymentModeForm()
    return render(request, 'payment_mode_form.html', {'form': form})

@login_required
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

@login_required
def payment_mode_delete(request, pk):
    payment_mode = get_object_or_404(PaymentMode, pk=pk)
    if request.method == "POST":
        payment_mode.delete()
        return redirect('payment_mode_list')
    return render(request, 'payment_mode_confirm_delete.html', {'payment_mode': payment_mode})


# for  bills pdf  generations
from django.http import HttpResponse
from .models import Bills, Receipt
from .utils import render_to_pdf, send_email_with_pdf_attachment

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
    
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Bills
from .forms import EmailPDFForm
from .utils import render_to_pdf  # Assuming this utility returns a PDF file as a HttpResponse
# import logging

# logger = logging.getLogger(__name__)
def email_pdf(request, pk):
    bill = get_object_or_404(Bills, pk=pk)
    
    # Generate the PDF content using your utility function.
    # Assuming `render_to_pdf` returns an HttpResponse with PDF content.
    response = bill_pdf_view(request, pk)
    if not isinstance(response, HttpResponse) or response.status_code != 200:
        return HttpResponse("Failed to generate PDF.", status=500)

    if request.method == 'POST':
        form = EmailPDFForm(request.POST)
        if form.is_valid():
            # Read PDF content from the response
            pdf_content = response.content
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_email = form.cleaned_data['recipient_list']  # assuming this field returns a single email string
            
            email = EmailMessage(subject, message, to=[recipient_email])
            email.attach('bill.pdf', pdf_content, 'application/pdf')
            # try:
            #     email.send()
            # except Exception as e:
            #     # Log the error or take appropriate actions
            #     logger.error(f"Failed to send email: {e}")
            email.send()

            
            return redirect('/')  # Assuming you have a 'home' view to redirect to after email is sent
    else:
        form = EmailPDFForm()
    
    return render(request, 'bills/email_form.html', {'form': form, 'bill': bill},)




def forgot_password_view(request):
    # If form is submitted
    if request.method == 'POST':
        # Process the form: verify email, send reset password link, etc.
        # Redirect to a new page or render the same page with a success message
        return redirect('success_page')
    else:
        # If GET request, show the form
        return render(request, 'forgot_password.html')

# All the code for send the email to user with reset password link
# Inside views.py of your Django app

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

def forgot_password_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Generate password reset token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
            # Construct the email content
            current_site = get_current_site(request)
            mail_subject = 'Password Reset'
            message = render_to_string('emails/password_reset_email.html', {
                'user': user,
                'domain': current_site.domain,
                'site_name': 'YourSiteName',
                'protocol': 'http',
                'path': f'/reset-password/{uid}/{token}/',
            })
            # Send the email
            send_mail(mail_subject, message, 'from@example.com', [email], fail_silently=False, html_message=message)
            # Redirect or respond indicating the email has been sent
            return redirect('email_sent_page')
    else:
        # Your form handling for GET requests here
        pass
    return render(request, 'forgot_password_form.html')





def success_page(request):
    # Your logic here
    return render(request, 'success_page.html')


# user profile page 


from .models import Profile
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # if not request.user.is_authenticated:
    #     return redirect('user_login')
    # # user_profile=Profile.objects.get(user=request.user)
   
    user_profile = Profile.objects.get(user=request.user)

    user_model=User.objects.get(username=request.user)
    if request.method=='POST':
        print("abc")    
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        if request.FILES.get('dp')==None:
            dp=user_profile.image
        else:
            dp=request.FILES.get('dp')
        user_profile.image=dp
        user_model.first_name=first_name
        user_model.last_name=last_name
        user_model.email=email

    user_model.save()
    user_profile.save()

    
    return render(request,'profile.html',{'user_profile':user_profile,'user_model':user_model})