from django.db import models

# Create your models here.

class Region(models.Model):
    ID_Region = models.AutoField(primary_key=True,verbose_name='Código de la Region')
    Region = models.CharField(max_length=20, blank=True, null=True)

class Comuna(models.Model):
    ID_Comuna = models.AutoField(primary_key=True,verbose_name='Código de la Comuna')
    Comuna = models.CharField(max_length=30)
    ID_Region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Direccion(models.Model):
    ID_Direccion = models.AutoField(primary_key=True,verbose_name='Código de la Dirección')
    Calle = models.CharField(max_length=30)
    Num_Casa = models.IntegerField()
    ID_Comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    ID_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Usuario(models.Model):
    ID_Usuario = models.AutoField(primary_key=True,verbose_name='Código del Usuario')
    Rut = models.IntegerField()
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)
    Num_Celular = models.IntegerField()
    Clave = models.CharField(max_length=30)
    ID_Rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    ID_Preguntas = models.ForeignKey(Preguntas,on_delete=models.CASCADE)

class Compra(models.Model):
    ID_Compra = models.AutoField(primary_key=True,verbose_name='Código de Compra')
    F_Entrega = models.DateField()
    F_Despacho = models.DateField()
    Estado = models.CharField(max_length=30)
    Total = models.CharField(max_length=30)
    Costo_Envio = models.CharField(max_length=30)
    Carro = models.CharField(max_length=30)
    ID_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Detalles(models.Model):
    ID_Detalle = models.AutoField(primary_key=True,verbose_name='Código Detalle')
    Cantidad = models.CharField(max_length=30)
    Subtotal = models.CharField(max_length=30)
    ID_Compra = models.ForeignKey(Compra,on_delete=models.CASCADE)

class Rol(models.Model):
    ID_Rol = models.AutoField(primary_key=True,verbose_name='Código del ROL')
    Rol = models.CharField(max_length=30)


class Preguntas(models.Model):
    ID_Preguntas = models.AutoField(primary_key=True,verbose_name='Código de Pregunta')
    Pregunta = models.CharField(max_length=30)

class Producto(models.Model):
    ID_Producto = models.AutoField(primary_key=True,verbose_name='Código del Producto')
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=30)
    Precio = models.CharField(max_length=30)
    Stock = models.CharField(max_length=30) 
    Foto = models.ImageField(upload_to="Producto")
    ID_Tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    ID_Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

class Categoria(models.Model):
    ID_Categoria = models.AutoField(primary_key=True,verbose_name='Código de la Categoria')
    Categoria = models.CharField(max_length=30)

class Tipo(models.Model):
    ID_Tipo = models.AutoField(primary_key=True,verbose_name='Código del Tipo')
    Tipo = models.CharField(max_length=30)