from django.db import models

# Create your models here.
from code.office.models import Cargo


class Person(models.Model):
    MALE = "M"
    FEMALE = "F"

    CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    name = models.CharField(max_length=40, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    age = models.IntegerField(blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=20, blank=False, null=False, choices=CHOICES)
    
    class Meta:
        verbose_name_plural = "Pessoas"
        verbose_name = "Pessoa"

        ordering = ["age"]

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, blank=False, null=False)
    salario = models.DecimalField(decimal_places=2, null=False, blank=False)
    cargo = models.ForeignKey(Cargo, blank=False, null=False, on_delete=models.PROTECT)

    class Meta: 
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

        ordering = ["cargo"]
