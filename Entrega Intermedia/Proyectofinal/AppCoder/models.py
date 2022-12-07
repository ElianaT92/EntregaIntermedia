from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Profesores(models.Model):
    nombre=models.CharField(max_length=40)
    asignatura=models.CharField(max_length=40)

class Egresados(models.Model):
    nombre=models.CharField(max_length=40)
    titulacion=models.CharField(max_length=40)

