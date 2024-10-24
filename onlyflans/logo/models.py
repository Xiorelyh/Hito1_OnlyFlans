from django.db import models

# Create your models here.
from django.db import models

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo
