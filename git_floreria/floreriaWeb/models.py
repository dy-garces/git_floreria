from pyexpat import model
from django.db import models
from datetime import datetime

from django.forms import IntegerField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imgen = models.ImageField(upload_to="productos",null=True)
    categoria =  models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
    
class Region(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    
class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    correo = models.EmailField()
    numero = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre

class Subcripcion(models.Model):
    num_sub = models.IntegerField(primary_key=True)
    descuento = models.IntegerField()
    
    def __str__(self):
        return self.num_sub
    
class Estado_subcripcion(models.Model):
    hora = datetime.now()
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    num_sub = models.ForeignKey(Subcripcion , on_delete=models.PROTECT)
    
    def __str__(self):
        return self.hora
    
class Vendedor(models.Model):
    rut_vendedor = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    correo = models.EmailField()
    numero = models.IntegerField()
    comuna = models.ForeignKey(Comuna,on_delete=models.PROTECT)

    def __str__(self):
        return self.rut_vendedor
    
class Proveedor(models.Model):
    fecha = models.DateField()
    hora = datetime.now()
    stock = models.IntegerField()
    rut_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fecha
########################################################################## VENTA   
class Venta(models.Model):
    num_venta = models.IntegerField(primary_key=True)
    hora = datetime.now()
    fecha = models.DateField()
    
    def __str__(self):
        return self.num_venta

class Detalle_Venta(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    descuento = models.IntegerField()
    total = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    num_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.cantidad
    
class Forma_Pago(models.Model):
    descripcion = models.CharField(max_length=20)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.descripcion
    
class Seguimiento_Compra(models.Model):
    id_seguimiento = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = datetime.now()
    estado = models.CharField(max_length=15)
    
    def __str__(self):
        return self.id_seguimiento
    
