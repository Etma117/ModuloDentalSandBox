from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta



# Create your models here.

class Clinica(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    responsables = models.ForeignKey('usuarios.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to='clinicas/', default='clinicas/default.jpg')
    #responsables = models.ManyToManyField('usuarios.CustomUser')  # Cambio aquí
    #logo = models.ImageField(upload_to='clinicas/', default='clinicas/default.jpg', blank=True, null=True)
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)
    equipamiento = models.CharField(max_length=255, null=True, blank=True)
    numero_consultorios = models.IntegerField(null=True)
    
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
    
    def dias_true(self):
        dias_true = []
        if self.lunes:
            dias_true.append('lunes')
        if self.martes:
            dias_true.append('martes')
        if self.miercoles:
            dias_true.append('miércoles')
        if self.jueves:
            dias_true.append('jueves')
        if self.viernes:
            dias_true.append('viernes')
        if self.sabado:
            dias_true.append('sábado')
        return dias_true
    
    def __str__(self):
        return self.nombre