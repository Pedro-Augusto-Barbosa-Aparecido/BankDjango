# Generated by Django 3.2.7 on 2021-10-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_person_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]