from django.contrib import admin

from .models import Account, Permissions

# Register your models here.

admin.site.register(Permissions)
admin.site.register(Account)
