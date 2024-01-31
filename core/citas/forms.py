from django import forms
from .models import Cita, HoraTrabajo
from usuarios.models import CustomUser
from clinicas.models import Clinica
from django.contrib.auth.models import Group

from datetime import datetime, timedelta


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'clinica', 'dentista', 'fecha', 'hora_trabajo','estado_cita'] 
        labels = {
            'paciente' : "Paciente",
            'dentista': "Dentista",
            'fecha' : "Fecha",  
            'clinica' : 'Clinicas',         
            'hora_trabajo' : "Seleciona un Horario Disponible",
            'estado_cita' : "Estado de la cita"

        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'dentista': forms.Select(attrs={'class': 'form-control'}),
            'clinica' : forms.Select(attrs={'class': 'form-control'}), 
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}, format='%Y-%m-%d'),
            'hora_trabajo' : forms.Select(attrs={'class': 'form-control'}),
            'estado_cita': forms.Select(attrs={'class': 'form-control'})
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar opciones del campo paciente según el grupo "pacientes"
        pacientes_group = Group.objects.get(name='Paciente')
        self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

        # Filtrar opciones del campo doctor según el grupo "doctores"
        dentista_group = Group.objects.get(name='Dentista')
        self.fields['dentista'].queryset = CustomUser.objects.filter(groups=dentista_group)

        # Calcula la fecha de mañana y establece como valor predeterminado
        tomorrow = (datetime.now() + timedelta(days=1)).date()
        self.initial['fecha'] = tomorrow


        # Filtrar los horarios de trabajo que no están ocupados
        self.fields['hora_trabajo'].queryset = HoraTrabajo.objects.filter(ocupada=False)

   

class CitaEditarForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'clinica', 'dentista', 'fecha', 'hora_trabajo','estado_cita'] 
        labels = {
            'paciente' : "Paciente",
            'dentista': "Dentista",
            'fecha' : "Fecha",  
            'clinica' : 'Clinicas',         
            'hora_trabajo' : "Horario Seleccionado",
            'estado_cita' : "Estado de la cita"


        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'dentista': forms.Select(attrs={'class': 'form-select'}),
            'clinica' : forms.Select(attrs={'class': 'form-select'}), 
             'fecha': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'hora_trabajo' : forms.Select(attrs={'class': 'form-control'}),
            'estado_cita': forms.RadioSelect(attrs={'class': 'form-check', 'type':'radio'})
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar opciones del campo paciente según el grupo "pacientes"
        pacientes_group = Group.objects.get(name='Paciente')
        self.fields['paciente'].queryset = CustomUser.objects.filter(groups=pacientes_group)

        # Filtrar opciones del campo doctor según el grupo "doctores"
        dentista_group = Group.objects.get(name='Dentista')
        self.fields['dentista'].queryset = CustomUser.objects.filter(groups=dentista_group)
