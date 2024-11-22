from django.db import models
from datetime import datetime

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    hhorario = models.DateTimeField()

    def __str__(self):
        return self.titulo