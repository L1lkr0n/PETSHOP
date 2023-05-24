from django.contrib import admin
<<<<<<< HEAD
from .models import Region,Comuna,Direccion,Usuario,Compra,Detalles,Rol,Preguntas,Producto,Categoria,Tipo
=======
from .models import models, Region, Comuna, Direccion, Compra, Detalles, Rol, Preguntas, Productos, Categoria, Tipo

>>>>>>> 14be853301c2a48fca6d66c185a4cf5669a512fe
# Register your models here.

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
<<<<<<< HEAD
admin.site.register(Usuario)
=======
>>>>>>> 14be853301c2a48fca6d66c185a4cf5669a512fe
admin.site.register(Compra)
admin.site.register(Detalles)
admin.site.register(Rol)
admin.site.register(Preguntas)
<<<<<<< HEAD
admin.site.register(Producto)
=======
admin.site.register(Productos)
>>>>>>> 14be853301c2a48fca6d66c185a4cf5669a512fe
admin.site.register(Categoria)
admin.site.register(Tipo)
