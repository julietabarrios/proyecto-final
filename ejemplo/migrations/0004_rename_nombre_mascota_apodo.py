# Generated by Django 4.1.3 on 2022-12-08 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0003_mascota_vehiculo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='nombre',
            new_name='apodo',
        ),
    ]