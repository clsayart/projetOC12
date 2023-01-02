from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    Gestion = 'Management'
    Commercial = 'Sales'
    Support = 'Support'

    RoleChoices = (
        (Gestion, 'Manager'),
        (Commercial, 'Salesperson'),
        (Support, 'Support')
    )

    role = models.CharField(max_length=64, choices=RoleChoices, null=False, verbose_name='role')

    def __str__(self):
        return f"User: {self.username} | Role: {self.role}"

# Create your models here.
