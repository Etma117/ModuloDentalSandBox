from django.db import models
from schedule.models import Calendar, Event

from usuarios.models import CustomUser
from clinicas.models import Clinica

class DiasNoLaborablesCalendar(Calendar):
    clinica = models.ForeignKey(Clinica, related_name='clinica_agenda_nolabor', on_delete=models.CASCADE)   

class DentistaCalendar(Calendar):
    dentista = models.ForeignKey(CustomUser, related_name='dentista_horario', on_delete=models.CASCADE, null=True, blank=True)
   
class CitasDentalesCalendar(Calendar):
    clinica = models.ForeignKey(Clinica, related_name='clinica_agenda', on_delete=models.CASCADE, null=True, blank=True) #obtener clinica usuario posterior
   
class Cita(Event):
     
    dentista = models.ForeignKey(CustomUser, related_name='agenda_dentista_citas', on_delete=models.CASCADE, null=True, blank=True)
    paciente = models.ForeignKey(CustomUser, related_name='agenda_paciente_citas', on_delete=models.CASCADE)

    clinica = models.ForeignKey(Clinica, related_name='agenda_clinica_cita', on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        slug_prefix = "citas_dentales_"
        # Intentar obtener el calendario por slug
        citas_dentales_calendar = CitasDentalesCalendar.objects.filter(slug=f"{slug_prefix}{self.clinica.id}").first()#calendario por clinica

        if citas_dentales_calendar:
            # El calendario "citas_dentales" ya existe, asignar su ID
            self.calendar_id = citas_dentales_calendar.id
        else:
            # El calendario "citas_dentales" no existe, crearlo y asignar su ID
            new_calendar = CitasDentalesCalendar.objects.create(name=f"Citas Dentales - {self.clinica.nombre}", slug=f"{slug_prefix}{self.clinica.id}", clinica=self.clinica) # Puedes personalizar el slug del calendario
            self.calendar_id = new_calendar.id

        # Llamada al método save de la clase padre para realizar la acción de guardado normal
        super().save(*args, **kwargs)