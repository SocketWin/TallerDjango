from django.db import models
from apps.archivo.models import Cliente, Producto
from django.contrib.auth.models import User

# Aquí se escribiran los modelos: Facturacion

class Factura(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    vendedor = models.ForeignKey(User)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2)
    iva = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)

class DetalleFactura(models.Model):
    codigo = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    precio_unit = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)