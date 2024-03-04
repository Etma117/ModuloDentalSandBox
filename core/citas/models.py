from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

from clinicas.models import Clinica
from usuarios.models import CustomUser


class HoraTrabajo(models.Model): ###Proximamente calcular con el horario dentista
    #dia_semana = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin}"

class Cita(models.Model):

    ESTADOS_CITA = (
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Espera', 'En Espera'),
        ('Concluida', 'Concluida')
    )

    dentista = models.ForeignKey(CustomUser, related_name='dentista_citas', on_delete=models.CASCADE, null=True, blank=True)
    paciente = models.ForeignKey(CustomUser, related_name='paciente_citas', on_delete=models.CASCADE)

    clinica = models.ForeignKey(Clinica, related_name='clinica_cita', on_delete=models.CASCADE)
   
    fecha = models.DateField(default=(datetime.now() + timedelta(days=1)).date()) 

    hora_trabajo = models.ForeignKey(HoraTrabajo, on_delete=models.CASCADE) #Selecionar un horario

    estado_cita = models.CharField(choices=ESTADOS_CITA, max_length=40, default='Espera')

    def __str__(self):
        return self.fecha   
    
    def save(self, *args, **kwargs):
        # Al guardar la cita, también marcamos el horario de trabajo como ocupado
        self.hora_trabajo.ocupada = True
        self.hora_trabajo.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Al eliminar la cita, marcamos el horario de trabajo como no ocupado
        self.hora_trabajo.ocupada = False
        self.hora_trabajo.save()
        super().delete(*args, **kwargs)