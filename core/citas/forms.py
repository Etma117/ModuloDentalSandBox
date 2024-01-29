from django import forms
from .models import Cita
from usuarios.models import CustomUser
from clinicas.models import Clinica
from django.contrib.auth.models import Group

from datetime import datetime, timedelta

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'clinica', 'doctor', 'fecha', 'hora_inicio', 'hora_termino', 'estado_cita'] 
        labels = {
            'paciente' : "Paciente",
            'doctor': "Doctor",
            'fecha' : "Fecha",  
            'clinica' : 'Clinicas',         
            'hora_inicio' : "Hora de inicio",
            'hora_termino' : "Hora de termino",
            'estado_cita' : "Estado de la cita"

        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'clinica' : forms.Select(attrs={'class': 'form-control'}), 
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'hora_inicio' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),            
            'hora_termino' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
            'estado_cita': forms.Select(attrs={'class': 'form-control'})
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar opciones del campo paciente según el grupo "pacientes"
        pacientes_group = Group.objects.get(name='Paciente')
        self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

        # Filtrar opciones del campo doctor según el grupo "doctores"
        doctores_group = Group.objects.get(name='Doctores')
        self.fields['doctor'].queryset = CustomUser.objects.filter(groups=doctores_group)

        # Calcula la fecha de mañana y establece como valor predeterminado
        tomorrow = (datetime.now() + timedelta(days=1)).date()
        self.initial['fecha'] = tomorrow
    
class CitaEditarForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'clinica', 'doctor', 'fecha', 'hora_inicio', 'hora_termino', 'estado_cita'] 
        labels = {
            'paciente' : "Paciente",
            'doctor': "Doctor",
            'fecha' : "Fecha",  
            'clinica' : 'Clinicas',         
            'hora_inicio' : "Hora de inicio",
            'hora_termino' : "Hora de termino",
            'estado_cita' : "Estado de la cita"

        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'clinica' : forms.Select(attrs={'class': 'form-select'}), 
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'hora_inicio' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),            
            'hora_termino' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
            'estado_cita': forms.RadioSelect(attrs={'class': 'form-check', 'type':'radio'})
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar opciones del campo paciente según el grupo "pacientes"
        pacientes_group = Group.objects.get(name='Paciente')
        self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

        # Filtrar opciones del campo doctor según el grupo "doctores"
        doctores_group = Group.objects.get(name='Doctores')
        self.fields['doctor'].queryset = CustomUser.objects.filter(groups=doctores_group)
