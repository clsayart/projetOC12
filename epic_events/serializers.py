from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Customer, Contract, Event


class CustomerListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'last_name', 'email']


class CustomerDetailSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                  'date_updated', 'sales_contact']


class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'customer', 'date_created', 'amount']


class ContractDetailSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'customer', 'date_created', 'date_updated', 'amount',
                  'status', 'payment_due', 'sales_contact']


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'customer', 'event_date']


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'customer', 'support_contact', 'event_status', 'event_date',
                  'date_created', 'date_updated', 'attendees', 'notes']

