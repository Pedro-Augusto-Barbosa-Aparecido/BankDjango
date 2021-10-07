from django.contrib import admin

from .models import Account, Permissions, Translations

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ("name", "permissions", "active")

admin.site.register(Permissions)
admin.site.register(Translations)
