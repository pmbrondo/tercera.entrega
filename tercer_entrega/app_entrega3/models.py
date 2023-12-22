from django.db import models

# Creo modelos, son tablas base de datos relacionables. Creo mis tablas!!

class Compositor(models.Model):
    nombre=models.CharField(max_length=30)
    disco=models.CharField(max_length=30)

class Temas(models.Model):
    nombre_tema=models.CharField(max_length=30)
    duracion=models.DurationField()
    



