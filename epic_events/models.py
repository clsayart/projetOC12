from django.db import models

from authentication.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=64, unique=True, null=False)
    mobile = models.CharField(max_length=64, unique=True, null=False)
    company_name = models.CharField(max_length=64, null=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False,
                                      related_name='customer_sales_contact')

    def __str__(self):
        return f"Client: {self.last_name} | Company: {self.company_name}"


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False,
                                      related_name='contract_sales_contact')
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=False,
                                 related_name='contract_customer')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateField(null=True)

    def __str__(self):
        return f"Client: {self.customer} | Statut Contrat: {self.status} | Sales Contact: {self.sales_contact}"


class Event(models.Model):
    InProgress = 'IN PROGRESS'
    Resolved = 'RESOLVED'

    StatusChoices = (
        (InProgress, 'In progress'),
        (Resolved, 'Resolved'),
    )

    # customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=False, related_name='event_customer')
    contract = models.ForeignKey(to=Contract, on_delete=models.RESTRICT, null=False, default='3', related_name='event_contract')
    # QUEL TYPE DE DELETE?
    # MIGRATION + objets créés avant?
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False,
                                        related_name='event_support_contact')
    event_status = models.CharField(max_length=64, choices=StatusChoices, default=InProgress)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.CharField(max_length=2048)

    def __str__(self):
        return f"Client: {self.contract} | Statut Event: {self.event_status} | Support Contact: {self.support_contact}"


# Create your models here.
