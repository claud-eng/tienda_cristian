# Generated by Django 4.2.10 on 2024-12-10 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaccion', '0002_producto_anio_producto_modelo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventaonline',
            name='estado_reserva',
            field=models.CharField(blank=True, choices=[('En proceso', 'En proceso'), ('Vendida', 'Vendida'), ('Desistida', 'Desistida')], default=None, max_length=20, null=True),
        ),
    ]