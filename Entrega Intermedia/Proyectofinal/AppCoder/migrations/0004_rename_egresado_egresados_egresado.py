# Generated by Django 4.1.3 on 2022-12-07 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_rename_diploma_egresados_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egresados',
            old_name='Egresado',
            new_name='egresado',
        ),
    ]
