"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bills import views 
from bills.views import receipt_charge_list, receipt_charge_create, receipt_charge_update, receipt_charge_delete
from bills.views import payment_mode_list, payment_mode_create, payment_mode_update, payment_mode_delete, bill_pdf_view, receipt_pdf_view

from django.urls import path
from django.contrib.auth import views as auth_views
from bills import views
from django.contrib.auth.views import LoginView, LogoutView

# from . import views  # Adjust this import based on your project structure


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('example/', views.example_view),
    path('', views.home, name='home'),  # Map the root URL to the home view
    # Include other URL patterns below

    # Your other URL patterns
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('register/', views.register, name='register'),

    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # All Charges URL 
    path('charges/', views.charge_list, name='charge_list'),
    path('charges/add/', views.charge_create, name='charge_create'),
    path('charges/<int:pk>/edit/', views.charge_update, name='charge_update'),
    path('charges/<int:pk>/delete/', views.charge_delete, name='charge_delete'),

# All Bills URL 
    path('bills/', views.bill_list, name='bill_list'),
    path('bills/add/', views.bill_create, name='bill_create'),
    path('bills/<int:pk>/edit/', views.bill_update, name='bill_update'),
    path('bills/<int:pk>/delete/', views.bill_delete, name='bill_delete'),

# All Bill_charges URL 
    path('bill_charges/', views.bill_charge_list, name='bill_charge_list'),
    path('bill_charges/add/', views.bill_charge_create, name='bill_charge_create'),
    path('bill_charges/<int:pk>/edit/', views.bill_charge_update, name='bill_charge_update'),
    path('bill_charges/<int:pk>/delete/', views.bill_charge_delete, name='bill_charge_delete'),

# All Receipts URL 
    path('receipts/', views.receipt_list, name='receipt_list'),
    path('receipts/add/', views.receipt_create, name='receipt_create'),
    path('receipts/<int:pk>/edit/', views.receipt_update, name='receipt_update'),
    path('receipts/<int:pk>/delete/', views.receipt_delete, name='receipt_delete'),

# All Receipt_charge URL 

    path('receipt_charge/', receipt_charge_list, name='receipt_charge_list'),
    path('receipt_charge/add/', receipt_charge_create, name='receipt_charge_create'),
    path('receipt_charge/<int:pk>/edit/', receipt_charge_update, name='receipt_charge_update'),
    path('receipt_charge/<int:pk>/delete/', receipt_charge_delete, name='receipt_charge_delete'),

# All Payment_mode URL 

    path('payment_mode/', payment_mode_list, name='payment_mode_list'),
    path('payment_mode/add/', payment_mode_create, name='payment_mode_create'),
    path('payment_mode/<int:pk>/edit/', payment_mode_update, name='payment_mode_update'),
    path('payment_mode/<int:pk>/delete/', payment_mode_delete, name='payment_mode_delete'),

# All PDF URL 
    path('bills/<int:pk>/pdf/', bill_pdf_view, name='bill_pdf'),
    path('receipts/<int:pk>/pdf/', receipt_pdf_view, name='receipt_pdf'),
    path('bill/<int:pk>/pdf/', bill_pdf_view, name='bill_pdf'),

]

