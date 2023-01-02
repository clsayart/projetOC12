from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .models import User


class EpicUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        managers = Group.objects.get(name='Managers')
        if user.role == "Management":
            user.is_staff = True
            user.save()
            managers.user_set.add(user)
        user.save()
        return user
