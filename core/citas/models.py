from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

from clinicas.models import Clinica
from usuarios.models import CustomUser

class Cita(models.Model):

    ESTADOS_CITA = (
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Espera', 'En Espera'),
        ('Concluida', 'Concluida')
    )

    doctor = models.ForeignKey(CustomUser, related_name='doctor_citas', on_delete=models.CASCADE)
    paciente = models.ForeignKey(CustomUser, related_name='paciente_citas', on_delete=models.CASCADE)

    clinica = models.ForeignKey(Clinica, related_name='clinica_cita', on_delete=models.CASCADE)
   
    fecha = models.DateField(default=(datetime.now() + timedelta(days=1)).date()) 
    hora_inicio = models.TimeField(default=timezone.now)
    hora_termino = models.TimeField(default=timezone.now)

    estado_cita = models.CharField(choices=ESTADOS_CITA, max_length=40, default='Espera')

    def __str__(self):
        return self.fecha   