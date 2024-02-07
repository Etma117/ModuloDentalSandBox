from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta

# Create your models here.

def limitar_opciones():
    return {'tipo_usuario': 'responsable'}

class Clinica(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    responsables = models.ForeignKey('usuarios.CustomUser', on_delete=models.CASCADE, null=True, blank=True,)
    logo = models.ImageField(upload_to='clinicas/', default='clinicas/default.jpg')
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)
    equipamiento = models.CharField(max_length=255, null=True, blank=True)
    numero_consultorios = models.IntegerField(null=True, help_text="Número de consultorios en la clínica (debe ser no negativo)")
    
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)

    def generar_horas_entre(self):
        hora_actual = datetime.combine(datetime.today(), self.hora_inicio)
        hora_fin = datetime.combine(datetime.today(), self.hora_fin)

        horas_entre = []
        while hora_actual <= hora_fin:
            horas_entre.append(hora_actual.time())
            hora_actual += timedelta(minutes=60)

        return horas_entre
    
    def __str__(self):
        return self.nombre