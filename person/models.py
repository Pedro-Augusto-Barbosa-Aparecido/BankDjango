from django.db import models

# Create your models here.
from office.models import Cargo
from accounts.models import Account


class Person(models.Model):
    MALE = "M"
    FEMALE = "F"

    CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    name = models.CharField(max_length=40, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    age = models.IntegerField(blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=20, blank=False, null=False, choices=CHOICES)
    active = models.BooleanField(default=True, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "Pessoas"
        verbose_name = "Pessoa"

        ordering = ["age"]

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    cargo = models.ForeignKey(Cargo, blank=False, null=False, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

        ordering = ["cargo"]

    def __str__(self) -> str:
        return f"{str(self.person)} - {self.cargo}"


class Client(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, blank=False, null=False)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, blank=False, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

        ordering = ["pk"]

    def __str__(self) -> str:
        return str(self.person)
