from django import forms
from .models import Clinica
from usuarios.models import CustomUser
from django.contrib.auth.models import Group

class clinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la clínica',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'correo_electronico': 'Correo electrónico',
            'equipamiento': 'Equipamiento',
            'numero_consultorios': 'Número de consultorios',
            'logo' : 'Logo de la Clínica'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo de la clínica'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección de la clínica'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Número de contacto'}),
            'hora_inicio': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'ejemplo@clinica.com'}),
            'equipamiento': forms.TextInput(attrs={'placeholder': 'Descripción del equipamiento'}),
            'numero_consultorios': forms.NumberInput(attrs={'min': '1', 'placeholder' : 'Cantidad de consultorios'}),
            'lunes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'martes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'miercoles': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'jueves': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'viernes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sabado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hora_inicio' : forms.TextInput(attrs={'placeholder':'Ej: 12:00:00'}),
            'hora_fin' : forms.TextInput(attrs={'placeholder':'Ej: 18:00:00'}),     
        } 
   # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)

     #   responsables_group = Group.objects.get(name='Responsable')
      #  self.fields['responsable'].queryset = CustomUser.objects.filter(groups=responsables_group)
