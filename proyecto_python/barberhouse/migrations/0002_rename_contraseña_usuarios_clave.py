# Generated by Django 4.0.6 on 2022-09-15 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barberhouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='contraseña',
            new_name='clave',
        ),
    ]
