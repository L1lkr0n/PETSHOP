from django.contrib import admin
from .models import models, Usuario,Region, Comuna, Direccion, Compra, Detalles, Rol, Preguntas, Productos, Categoria, Tipo

# Register your models here.

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Compra)
admin.site.register(Detalles)
admin.site.register(Rol)
admin.site.register(Preguntas)
admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Usuario)