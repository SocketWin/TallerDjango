# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps.archivo.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('razon_social', models.CharField(blank=True, null=True, max_length=50)),
                ('cedula_ruc', models.CharField(max_length=13)),
                ('direccion', models.CharField(blank=True, null=True, max_length=50)),
                ('telefono', models.CharField(blank=True, null=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, null=True, max_length=150)),
                ('marca', models.CharField(blank=True, null=True, max_length=30)),
                ('tipo', models.CharField(max_length=1, choices=[('F', 'Físico'), ('S', 'Servicio')])),
                ('precio_costo', models.DecimalField(max_digits=7, blank=True, null=True, decimal_places=2)),
                ('precio_venta', models.DecimalField(max_digits=7, blank=True, null=True, decimal_places=2)),
                ('porcent_utilidad', models.DecimalField(max_digits=4, blank=True, null=True, decimal_places=2)),
                ('stock', models.IntegerField(blank=True, null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('biografia', models.CharField(max_length=150)),
                ('foto', models.ImageField(upload_to=apps.archivo.models.ProfileUser.url, blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
