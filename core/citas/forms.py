from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'doctor', 'fecha', 'hora_inicio', 'hora_termino', 'estado_cita'] 
        labels = {
            'paciente' : "Paciente",
            'doctor': "Doctor",
            'fecha' : "Fecha",            
            'hora_inicio' : "Hora de inicio",
            'hora_termino' : "Hora de termino",
            'estado_cita' : "Estado de la cita"

        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'hora_inicio' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),            
            'hora_termino' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
            'estado_cita': forms.Select(attrs={'class': 'form-control'})
            
        }