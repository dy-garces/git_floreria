from django.contrib import admin
from .models import Categoria,Producto,Region,Comuna,Cliente,Venta,Vendedor,Seguimiento_Compra,Subcripcion,Estado_subcripcion,Proveedor,Detalle_Venta,Forma_Pago
# Register your models here.


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Venta)
admin.site.register(Seguimiento_Compra)
admin.site.register(Subcripcion)
admin.site.register(Estado_subcripcion)
admin.site.register(Proveedor)
admin.site.register(Detalle_Venta)
admin.site.register(Forma_Pago)