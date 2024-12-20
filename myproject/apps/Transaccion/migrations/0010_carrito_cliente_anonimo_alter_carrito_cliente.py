# Generated by Django 4.2.10 on 2024-12-16 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_clienteanonimo'),
        ('Transaccion', '0009_ventamanual_cliente_anonimo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cliente_anonimo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuario.clienteanonimo'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuario.cliente'),
        ),
    ]
