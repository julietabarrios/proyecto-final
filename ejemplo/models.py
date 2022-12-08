from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.numero_pasaporte}, {self.id}"

class Dummy (models.Model):
    nombre = models.CharField(max_length=100)

class Mascota(models.Model):
    apodo = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
    
    def __str__(self):
      return f"{self.apodo}, {self.raza}, {self.edad}, {self.id}"

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    patente = models.CharField(max_length=10)
    
    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.patente}, {self.id}"