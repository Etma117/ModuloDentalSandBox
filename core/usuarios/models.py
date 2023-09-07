from django.contrib.auth.models import AbstractUser
from django.db import models
from clinicas.models import Clinica
# Create your models here.

class CustomUser(AbstractUser):
    TIPOS_USUARIO = (
        ('administrador', 'Administrador'),
        ('medico', 'Médico'),
        ('asistente', 'Asistente'),
        ('paciente', 'Paciente'),
    )

    tipo_usuario = models.CharField(choices=TIPOS_USUARIO, max_length=15)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    clinicas = models.ManyToManyField(Clinica)

    def __str__(self):
        return self.username