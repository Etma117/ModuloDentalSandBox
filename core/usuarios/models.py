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
    foto = models.ImageField(upload_to='usuarios/fotos/', null=True, blank=True)
    clinicas = models.ManyToManyField(Clinica)
    

    def __str__(self):
        return self.username
    

class Administrador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dato_especifico_admin = models.CharField(max_length=255)

class Medico(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cedula_profesional = models.CharField(max_length=255)

class Asistente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dato_especifico_asistente = models.CharField(max_length=255)

class Paciente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dato_especifico_paciente = models.CharField(max_length=255)