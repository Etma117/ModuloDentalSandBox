from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Clinica(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    horario = models.CharField(max_length=10, null=True, blank= True)
    responsable = models.CharField(max_length=100, null=True, blank= True)
    logo = models.ImageField(upload_to='clinicas/', default='clinicas/default.jpg')
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)
    #servicios_ofrecidos = models.Char
    equipamiento = models.CharField(max_length=255, null=True, blank=True)
    numero_consultorios = models.IntegerField(null=True , validators=[MinValueValidator(1)],help_text="Número de consultorios en la clínica (debe ser no negativo)")

    def __str__(self):
        return self.nombre