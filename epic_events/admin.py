from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer, Contract, Event
from .forms import CustomerCreationForm, ContractCreationForm, EventCreationForm


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    form = CustomerCreationForm

    list_display = ['sales_contact', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created']
    list_filter = ['sales_contact', 'company_name']
    search_fields = ['first_name', 'last_name']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    model = Contract
    form = ContractCreationForm

    list_display = ['customer', 'sales_contact', 'amount', 'status', 'payment_due']
    list_filter = ['customer', 'sales_contact', 'amount', 'status', 'payment_due']
    search_fields = ['customer']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    form = EventCreationForm

    list_display = ['customer', 'support_contact', 'event_status', 'event_date', 'attendees', 'notes']
    list_filter = ['customer', 'support_contact', 'event_status', 'event_date']
    search_fields = ['customer']
