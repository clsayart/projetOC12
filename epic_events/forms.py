from django import forms

from authentication.models import User
from .models import Customer, Contract, Event


class CustomerCreationForm(forms.ModelForm):
    sales_contact = forms.ModelChoiceField(queryset=User.objects.filter(role='Sales'))

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact')


class ContractCreationForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    sales_contact = forms.ModelChoiceField(queryset=User.objects.filter(role='Sales'))

    class Meta:
        model = Contract
        fields = ('customer', 'sales_contact', 'amount', 'status', 'payment_due')


class EventCreationForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    support_contact = forms.ModelChoiceField(queryset=User.objects.filter(role='Support'))

    class Meta:
        model = Event
        fields = ('customer', 'support_contact', 'event_status', 'event_date', 'attendees', 'notes')
