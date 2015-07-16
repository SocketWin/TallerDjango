from django.db import models
from django.contrib.auth.models import User
# Aquí se escribiran los modelos: Productos, Clientes, Usuarios


class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    marca = models.CharField(max_length=30, null=True, blank=True)
    TIPO_ITEMS = (
        ('F', 'Físico'),
        ('S', 'Servicio'),
    )
    tipo = models.CharField(max_length=1, choices=TIPO_ITEMS)
    precio_costo = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    precio_venta = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    porcent_utilidad = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(editable=False, null=True, blank=True)

class Clientes(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50, null=True, blank=True)
    cedula_ruc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

class ProfileUser(models.Model):
    user = models.OneToOneField(User)
    biografia = models.CharField(max_length=150)
    def url(self, filename):
        ruta = "Users/%s/%s" % (self.user.username, filename)
    foto = models.ImageField(upload_to=url, null=True, blank=True)