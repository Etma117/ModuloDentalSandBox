from django.contrib.auth.models import AbstractUser
from django.db import models
from clinicas.models import Clinica
# Create your models here.
from django.conf import settings




class CustomUser(AbstractUser):
    TIPOS_USUARIO = (
        ('administrador', 'Administrador'),
        ('medico', 'Médico'),
        ('asistente', 'Asistente'),
        ('paciente', 'Paciente'),
        ('responsable', 'Responsable')
    )
    apellido_materno = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    celular = models.CharField(max_length=20, blank=True)
    telefono_fijo = models.CharField(max_length=20, blank=True)

    tipo_usuario = models.CharField(choices=TIPOS_USUARIO, max_length=15)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True, verbose_name='No. celular')
    foto = models.ImageField(upload_to='usuarios/fotos/', null=True, blank=True)
    clinicas = models.ManyToManyField(Clinica, related_name='usuarios_asignados')
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_users',
        verbose_name='Creado por'
    )

    def contar_clinicas_asignadas(self):
        if self.tipo_usuario == 'responsable':
            return self.clinicas.count()
        else:
            return 0

    SEX_CHOICES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        # Puedes agregar más opciones si es necesario
    ]
    sexo = models.CharField(max_length=10, choices=SEX_CHOICES, blank=True, verbose_name='Genero')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')

    PREGUNTAS_SEGURIDAD_1 = [
        ('nombre_primera_mascota', '¿Cuál es el nombre de tu primera mascota?'),
        ('ciudad_nacimiento', '¿En qué ciudad naciste?'),
        ('nombre_mejor_amigo', '¿Cómo se llama tu mejor amigo de la infancia?'),
    ]

    PREGUNTAS_SEGURIDAD_2 = [
        ('primer_coche', '¿Cuál fue la marca de tu primer coche?'),
        ('primera_escuela', '¿Cómo se llama tu primera escuela?'),
        ('plato_favorito', '¿Cuál es tu plato favorito?'),
    ]

    pregunta_seguridad_1 = models.CharField(max_length=255, choices=PREGUNTAS_SEGURIDAD_1, blank=True, null=True)
    respuesta_seguridad_1 = models.CharField(max_length=255, blank=True,  null=True)
    pregunta_seguridad_2 = models.CharField(max_length=255, choices=PREGUNTAS_SEGURIDAD_2, blank=True, null=True)
    respuesta_seguridad_2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    
class AsistenteDentista(models.Model):
    asistente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='asistente_dentistas')
    dentista = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dentista_asistentes')

    def __str__(self):
        return f"{self.asistente.username} asiste a {self.dentista.username}"

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