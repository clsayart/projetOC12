from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
import datetime

from .models import Customer, Contract, Event
from .serializers import CustomerListSerializer, CustomerDetailSerializer, ContractListSerializer, \
    ContractDetailSerializer, EventListSerializer, EventDetailSerializer
from authentication.models import User
from authentication.permissions import CustomerPermissions, ContractPermissions, EventPermissions


class CustomerViewSet(ModelViewSet):

    lookup_view_s = 'customer'
    permission_classes = [IsAuthenticated, CustomerPermissions]
    serializer_class = CustomerListSerializer
    detail_serializer_class = CustomerDetailSerializer
    queryset = Customer.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('last_name', 'email')

    def create(self, request, *args, **kwargs):
        print("request", request.data)
        print("data create", request.data)
        serializer = CustomerDetailSerializer(data=request.data)
        request.data['sales_contact'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print("instance update", instance)
        data = request.data
        print("data", data)

        try:
            sales_contact = User.objects.get(id=data['sales_contact'])
            if sales_contact.role == 'Sales':
                instance.sales_contact = sales_contact
        except KeyError:
            sales_contact = User.objects.get(id=request.user.id)
            if sales_contact.role == 'Sales':
                instance.sales_contact = sales_contact

        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.email = data.get('email', instance.email)
        instance.phone = data.get('phone', instance.phone)
        instance.mobile = data.get('mobile', instance.mobile)
        instance.company_name = data.get('company_name', instance.company_name)

        serializer = CustomerDetailSerializer(instance)
        print("serializer", serializer)
        instance.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("instance destroy", instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            print("retrieve get serializer")
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContractViewSet(ModelViewSet):

    lookup_url_kwarg = 'contract'
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('customer', 'date_created', 'amount')

    def create(self, request, *args, **kwargs):
        print(kwargs)
        serializer = ContractDetailSerializer(data=request.data)
        request.data['sales_contact'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        print("req, args, kwargs", request, args, kwargs)
        instance = self.get_object()
        print("instance", instance)
        data = request.data
        print("data", data)

        try:
            customer = Customer.objects.get(id=data['customer'])
            instance.customer = customer
        except KeyError:
            pass

        try:
            sales_contact = User.objects.get(id=data['sales_contact'])
            if sales_contact.role == 'Sales':
                instance.sales_staff = sales_contact
        except KeyError:
            sales_contact = User.objects.get(id=request.user.id)
            if sales_contact.role == 'Sales':
                instance.sales_contact = sales_contact

        print(data['amount'])
        print(data['status'])
        print(data['payment_due'])
        instance.amount = data['amount']
        instance.status = data['status']
        instance.payment_due = data['payment_due']
        # try:
        #     instance.amount = data['amount']
        # except KeyError:
        #     instance.amount = instance.amount
        #gestion des key-errors?

        serializer = ContractDetailSerializer(instance)
        instance.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    # try remove and see if still works


class EventViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated, EventPermissions]
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('event_date', 'customer')

    def create(self, request, *args, **kwargs):
        serializer = EventDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        try:
            customer = Customer.objects.get(id=data['customer'])
            instance.customer = customer
        except KeyError:
            pass

        try:
            support_contact = User.objects.get(id=data['support_contact'])
            if support_contact.role == 'Support':
                instance.support_contact = support_contact
        except KeyError:
            support_contact = User.objects.get(id=request.user.id)
            if support_contact.role == 'Support':
                instance.sales_contact = support_contact

        instance.status = data.get('status', instance.status)
        instance.attendees = data.get('attendees', instance.attendees)
        instance.notes = data.get('notes', instance.notes)
        serializer = EventDetailSerializer(instance)
        instance.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


