from django import forms
from .models import Cita
from usuarios.models import CustomUser
from clinicas.models import Clinica
from django.contrib.auth.models import Group

from .widgets import SplitDateTimeWidgetCustom

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
        fields = ['paciente','clinica','dentista','start', 'end', 'title', 'description', 'creator', 'estado_cita',
                  'color_event'] 
      

        labels = {
            'paciente': 'Paciente',
            'clinica': 'Clínica',
            'dentista': 'Dentista',
            'start': 'Fecha',
            'end': 'Fecha de Fin',
            'title': 'Título',
            'description': 'Descripción',
            'creator': 'Creador',
            'estado_cita' :'Estado de la cita',
            'color_event': 'Color',
        }

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'clinica': forms.Select(attrs={'class': 'form-control'}),
            'dentista': forms.Select(attrs={'class': 'form-control'}),
            'start': SplitDateTimeWidgetCustom(attrs={'class': 'datetime-input'}),
            'end': SplitDateTimeWidgetCustom(attrs={'class': 'datetime-input'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'estado_cita': forms.Select(attrs={'class': 'form-control'}),
            'color_event': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar opciones del campo paciente según el grupo "pacientes"
        pacientes_group = Group.objects.get(name='Paciente')
        self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

        # Filtrar opciones del campo doctor según el grupo "doctores"
        dentista_group = Group.objects.get(name='Dentista')
        self.fields['dentista'].queryset = CustomUser.objects.filter(groups=dentista_group)

    


class CitaEditarForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente','clinica','dentista','start', 'end', 'title', 'description', 'creator', 'estado_cita',
                  'color_event'] 
        
        labels = {
            'paciente': 'Paciente',
            'clinica': 'Clínica',
            'dentista': 'Dentista',
            'start': 'Fecha',
            'end': 'Fecha de Fin',
            'title': 'Título',
            'description': 'Descripción',
            'creator': 'Creador',
            'estado_cita' :'Estado de la cita',
            'color_event': 'Color',
        }

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'clinica': forms.Select(attrs={'class': 'form-control'}),
            'dentista': forms.Select(attrs={'class': 'form-control'}),
            'start': SplitDateTimeWidgetCustom(attrs={'class': 'datetime-input'}),
            'end': SplitDateTimeWidgetCustom(attrs={'class': 'datetime-input'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'estado_cita': forms.Select(attrs={'class': 'form-control'}),
            'color_event': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Filtrar opciones del campo paciente según el grupo "pacientes"
            pacientes_group = Group.objects.get(name='Paciente')
            self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

            # Filtrar opciones del campo doctor según el grupo "doctores"
            dentista_group = Group.objects.get(name='Dentista')
            self.fields['dentista'].queryset = CustomUser.objects.filter(groups=dentista_group)

from schedule.models import Rule

class HorarioLaborableForm(forms.ModelForm):

    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Hora de inicio')
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Hora de fin')

    class Meta:
        model = Rule
        fields = ['name', 'description', 'params']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['params'].widget = forms.CheckboxSelectMultiple(choices=[
            ('MO', 'Lunes'),
            ('TU', 'Martes'),
            ('WE', 'Miércoles'),
            ('TH', 'Jueves'),
            ('FR', 'Viernes'),
            ('SA', 'Sábado'),
            ('SU', 'Domingo'),
        ])