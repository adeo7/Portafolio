from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class proyectos(models.Model):
    titulo =models.CharField(max_length=100)
    descripcion=models.CharField(max_length=250)
    imagen=models.ImageField(upload_to="porfolio/imagenes/") 
    url=models.URLField(blank=True)
