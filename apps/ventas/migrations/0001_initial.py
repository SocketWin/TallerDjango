# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('archivo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unit', models.DecimalField(max_digits=5, decimal_places=2)),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('iva', models.DecimalField(max_digits=7, decimal_places=2)),
                ('total', models.DecimalField(max_digits=7, decimal_places=2)),
                ('cliente', models.ForeignKey(to='archivo.Clientes')),
                ('vendedor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(to='ventas.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(to='archivo.Producto'),
        ),
    ]
