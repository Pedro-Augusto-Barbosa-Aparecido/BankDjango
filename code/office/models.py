from django.db import models

# Create your models here.


class Cargo(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
