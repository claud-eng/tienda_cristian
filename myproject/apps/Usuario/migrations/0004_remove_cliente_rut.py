# Generated by Django 4.2.10 on 2024-12-22 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_clienteanonimo_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='rut',
        ),
    ]