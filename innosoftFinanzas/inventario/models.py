from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre= models.CharField(max_length=70)
    categoria = models.CharField(max_length=70)
    unidades = models.IntegerField()
    valorMonetario = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Necesidad(models.Model):
    nombre = models.CharField(max_length=70)
    comite = models.CharField(max_length=70)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre