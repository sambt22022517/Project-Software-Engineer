# Generated by Django 5.0.3 on 2024-03-23 01:27

from django.db import migrations


def create_data(apps, schema_editor):
    Customers = apps.get_model('customers', 'Customer')
    Customers(name="Joe Silver", email="joe@email.com", document="22342342", phone="00000000").save()


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
