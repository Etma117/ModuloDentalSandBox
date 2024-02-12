from django import forms
from .models import Cita
from usuarios.models import CustomUser
from clinicas.models import Clinica
from django.contrib.auth.models import Group

from datetime import datetime, timedelta

#    start, end, title, description
    #creator
    #created_on
    #updated_on
    #rule
    #end_recurring_period
    #calendar
    #color_event
    
    #dentista 
    #paciente 
    #clinica

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente','clinica','dentista','start', 'end', 'title', 'description', 'creator',
                  'color_event'] 
        fields = [
    'paciente', 'clinica', 'dentista', 'start', 'end', 'title', 'description', 'creator', 'color_event'
        ]

        labels = {
            'paciente': 'Paciente',
            'clinica': 'Clínica',
            'dentista': 'Dentista',
            'start': 'Fecha',
            'end': 'Fecha de Fin',
            'title': 'Título',
            'description': 'Descripción',
            'creator': 'Creador',
            'color_event': 'Color',
        }

        placeholders = {
            'paciente': 'Seleccione al paciente',
            'clinica': 'Seleccione la clínica',
            'dentista': 'Seleccione al dentista',
            'start': 'Seleccione la fecha y hora de inicio',
            'end': 'Seleccione la fecha y hora de fin',
            'title': 'Ingrese el título del evento',
            'description': 'Ingrese la descripción del evento',
            'creator': 'Seleccione al creador del evento',
            'color_event': 'Ingrese el color del evento',
        }

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'clinica': forms.Select(attrs={'class': 'form-control'}),
            'dentista': forms.Select(attrs={'class': 'form-control'}),
            #'start': forms.SplitDateTimeWidget(attrs={'class': 'datetime-input'}),
            #'end': forms.SplitDateTimeWidget(attrs={'class': 'datetime-input'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'color_event': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            request = kwargs.pop('request')

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Filtrar opciones del campo paciente según el grupo "pacientes"
        pacientes_group = Group.objects.get(name='Paciente')
        self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

        # Filtrar opciones del campo doctor según el grupo "doctores"
        dentista_group = Group.objects.get(name='Dentista')
        self.fields['dentista'].queryset = CustomUser.objects.filter(groups=dentista_group)

        # Calcula la fecha de mañana y establece como valor predeterminado
        #tomorrow = (datetime.now() + timedelta(days=1)).date()
        #self.initial['fecha'] = tomorrow


        # Filtrar los horarios de trabajo que no están ocupados
       # self.fields['hora_trabajo'].queryset = HoraTrabajo.objects.filter(ocupada=False)

   

