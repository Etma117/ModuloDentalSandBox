#Django clases
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
#Models
from schedule.models import Calendar, Event
from .models import Cita
from .forms import CitaForm
#librerias externas
import datetime
import pytz



class EventosView(ListView):
    model=Cita
    context_object_name = 'citas'
    template_name = 'agenda.html'

    def get_queryset(self):
        return Cita.objects.all().order_by('start') #user=self.request.user clinica, dentista filtro 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendars = Calendar.objects.all()
        events = Event.objects.filter(calendar__in=calendars)
        non_working_calendar = Calendar.objects.get(name="Dias No Laborables")
        dentista_calendario= Calendar.objects.get(name="Horario Dentista")

        context['events_json'] = self.serialize_events(events, non_working_calendar, dentista_calendario)
        return context
    

    def serialize_events(self, events, non_working_calendar, dentista_calendario ):
        serialized_events = []
        tz = pytz.timezone('America/Mexico_City')

        for event in events:

            for occurrence in event.get_occurrences(datetime.datetime(2024,1,1,0,0, tzinfo=tz), datetime.datetime(2025,1,1,0,0, tzinfo=tz) ): #marcar limites de fecha para motrar
               # print(occurrence, event.title)   

                serialized_event = {
                    'id': event.id,
                    'title': event.title,
                    'start': occurrence.start.isoformat(),
                    'end': occurrence.end.isoformat(),
                    'display': 'block',
                    'color': event.color_event
                }

                # Añadir el atributo 'display' solo para eventos del calendario de días no laborables
                if non_working_calendar.event_set.filter(id=event.id).exists():
                    serialized_event['allDay'] = 'allDay'
                    serialized_event['display'] = 'background'
                    serialized_event['backgroundColor'] = 'red'   

                if dentista_calendario.event_set.filter(id=event.id).exists():
                    serialized_event['title'] = ' '
                    serialized_event['allDay'] = 'allDay'
                    serialized_event['display'] = 'background' 

                serialized_events.append(serialized_event)

        return serialized_events
    

class CitaCrearView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'crear_cita.html'  # Reemplaza con el nombre de tu plantilla
    success_url = reverse_lazy('Agenda')

    def form_valid(self, form):
        # Asignar la clínica al calendario de citas
        #clinica = self.request.user.clinica  # Ajusta según cómo obtienes la clínica del usuario
        #form.instance.calendar = clinica.citas_dentales_calendar  # Ajusta según la relación real en tu modelo
        return super().form_valid(form)


