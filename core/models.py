from django.db import models

# Create your models here.

class Colaboradores(models.Model):

    rutColaborador =  models.CharField(primary_key=True,max_length=10, verbose_name='Rut del Colaborador')
    image = models.ImageField(upload_to='img',verbose_name='Imagen')
    nombre = models.CharField(max_length=70,verbose_name='Nombre Completo')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    correo = models.CharField(max_length=30, verbose_name='Correo')
    pais = models.CharField(max_length=30, verbose_name='País')
    contraseña = models.CharField(max_length=20, verbose_name='Contraseña')

    def str(self):
        return self.rutColaborador