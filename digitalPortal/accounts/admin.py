from django.contrib import admin

from digitalPortal.accounts.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'creation_date')
