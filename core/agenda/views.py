#Django clases
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
#Models
from schedule.models import Calendar, Event
from .models import Cita, DentistaCalendar, CitasDentalesCalendar, DiasNoLaborablesCalendar
from .forms import CitaForm, CitaEditarForm
from usuarios.models import CustomUser 
#librerias externas
import datetime
import pytz



class EventosView(ListView):
    model=Cita
    context_object_name = 'citas'
    template_name = 'agenda.html'

    def get_queryset(self):
        # Obtener el usuario que inició sesión
        usuario_actual = self.request.user

        # Filtrar las citas por el usuario actual
        return Cita.objects.filter(dentista=usuario_actual).order_by('start')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario_actual = CustomUser.objects.get(id=self.request.user.id)
        clinicas_usuario = usuario_actual.clinicas.all()

    # Obtener todos los eventos y calendarios necesarios de antemano
        HorarioDentista = DentistaCalendar.objects.filter(dentista=usuario_actual)
        Citasclinica= CitasDentalesCalendar.objects.filter(clinica__in=clinicas_usuario)

        horario= Event.objects.filter(calendar__in=HorarioDentista)
        
        citas = Event.objects.filter(calendar__in=Citasclinica )
        context['events_json'] = self.serialize_events(citas, horario)
        return context
    

    def serialize_events(self, citas, horario):
        serialized_events = []
        tz = pytz.timezone('America/Mexico_City')

        for event in citas:
            for occurrence in event.get_occurrences(datetime.datetime(2024,1,1,0,0, tzinfo=tz), datetime.datetime(2025,1,1,0,0, tzinfo=tz) ): #marcar limites de fecha para motrar
            
                serialized_event = {
                    'id': event.id,
                    'title': event.title,
                    'start': occurrence.start.isoformat(),
                    'end': occurrence.end.isoformat(),
                    'display': 'block',
                    'color': event.color_event
                }
                # Añadir el atributo 'display' solo para eventos del calendario de días no laborables
                # if non_working_calendar.event_set.filter(id=event.id).exists():
                #     serialized_event['allDay'] = 'allDay'
                #     serialized_event['display'] = 'background'
                #     serialized_event['backgroundColor'] = 'red'
                
                serialized_events.append(serialized_event)  

        for event in horario:
            for occurrence in event.get_occurrences(datetime.datetime(2024,1,1,0,0, tzinfo=tz), datetime.datetime(2025,1,1,0,0, tzinfo=tz) ):
                serialized_event = {
                        'id': event.id,
                        'title': '',
                        'start': occurrence.start.isoformat(),
                        'end': occurrence.end.isoformat(),
                        
                        'allDay':'allDay',
                        'display': 'background',
                        'color': event.color_event                     
                    }
                serialized_events.append(serialized_event)
           
            

                 
                
        return serialized_events
    

class CitaCrearView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'crear_cita.html'  # Reemplaza con el nombre de tu plantilla
    success_url = reverse_lazy('Agenda')

    def form_valid(self, form):
        # Obtén los datos del formulario
        start = form.cleaned_data['start']
        end = form.cleaned_data['end']
        dentista = form.cleaned_data['dentista']

        # Verifica si hay una cita existente en el mismo horario con estado 'aprobado'
        if Cita.objects.filter( #usar el calendario de citas de clinca 
                start__lt=end,
                end__gt=start,
                dentista=dentista, #puede haber citas en el mismo horario pero con dentista diferente
                estado_cita='Aprobada'
        ).exists():
            form.add_error(None, 'Ya hay una cita aprobada en ese horario con ese dentista.')
            return self.form_invalid(form)

        # Llama al método form_valid del padre para guardar la cita
        return super().form_valid(form)

class CitaEditarView(UpdateView):
    model = Cita
    form_class = CitaEditarForm
    template_name = 'editar_cita.html'  # Reemplaza con el nombre de tu plantilla
    success_url = reverse_lazy('Agenda')

    def form_valid(self, form):
        # Asignar la clínica al calendario de citas
        #clinica = self.request.user.clinica  # Ajusta según cómo obtienes la clínica del usuario
        #form.instance.calendar = clinica.citas_dentales_calendar  # Ajusta según la relación real en tu modelo
        return super().form_valid(form)