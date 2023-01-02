from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import EpicUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = EpicUserCreationForm
    list_display = ['username', 'email', 'role', 'is_staff', 'id']
    fieldsets = (*UserAdmin.fieldsets, (None, {'fields': ('role',)}))

    add_fieldsets = (*UserAdmin.add_fieldsets, (None, {'fields': ('role',)}))


admin.site.register(User, CustomUserAdmin)
