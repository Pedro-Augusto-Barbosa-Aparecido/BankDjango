from django.db import models

# Create your models here.
class Permissions(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = "Permissão"
        verbose_name_plural = "Permissões"

        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    permissions = models.ForeignKey(Permissions, on_delete=models.PROTECT, blank=False, null=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0.0)
    number = models.CharField(max_length=10, blank=False, null=False, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

        ordering = ["name", "number"]

    def __str__(self) -> str:
        return self.name

class Translations(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, blank=False, null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = "Transferência"
        verbose_name_plural = "Transferências"

        ordering = ["value"]

    def __str__(self) -> str:
        return f"Transferência {self.pk}"    
