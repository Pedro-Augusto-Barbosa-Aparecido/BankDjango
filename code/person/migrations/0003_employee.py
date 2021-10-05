# Generated by Django 3.2.8 on 2021-10-05 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
        ('person', '0002_alter_person_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='office.cargo')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': ['cargo'],
            },
        ),
    ]
