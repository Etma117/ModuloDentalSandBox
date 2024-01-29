from django.db import models

# Create your models here.

class Clinica(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    horario = models.CharField(max_length=10, null=True, blank= True)
    responsable = models.CharField(max_length=100, null=True, blank= True)
    logo = models.ImageField(upload_to = 'clinicas/', default='clinicas/default.jpg')

    def __str__(self):
        return self.nombre