from django.db import models
from usuarios.models import CustomUser
from django.conf import settings


# Create your models here.


class Cita(models.Model):

    ESTADOS_CITA = (
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Espera', 'En Espera'),
        ('Concluida', 'Concluida')
    )

    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#models.CharField(max_length=255, blank=True) #models.ForeignKey(settings.AUTH_USER_MODEL)
    doctor = models.CharField(max_length=255, blank=True)  #models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    fecha = models.DateField()  
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    estado_cita = models.CharField(choices=ESTADOS_CITA, max_length=40)

    #def __str__(self):
        #return self.paciente