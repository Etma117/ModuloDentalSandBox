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
    responsables = models.ManyToManyField('usuarios.CustomUser', blank=True)
    logo = models.ImageField(upload_to='clinicas/', default='clinicas/default.jpg', blank=True, null=True)
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)
    equipamiento = models.CharField(max_length=255, null=True, blank=True)
    numero_consultorios = models.IntegerField(null=True , validators=[MinValueValidator(1)],help_text="Número de consultorios en la clínica (debe ser no negativo)")

    def generar_horas_entre(self):
        hora_actual = datetime.combine(datetime.today(), self.hora_inicio)
        hora_fin = datetime.combine(datetime.today(), self.hora_fin)

        horas_entre = []
        while hora_actual <= hora_fin:
            horas_entre.append(hora_actual.time())
            hora_actual += timedelta(minutes=60)

        return horas_entre
    
    def contar_clinicas_asignadas(cls, responsable):
        if responsable.tipo_usuario == 'responsable':
            return cls.objects.filter(responsable=responsable).count()
        else:
            return 0
    
    def __str__(self):
        return self.nombre