from django.contrib import admin

from .models import Client, Employee, Person

# Register your models here.

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Client)
