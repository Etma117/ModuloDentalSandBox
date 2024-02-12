from django import forms
from .models import Clinica
from usuarios.models import CustomUser
from django.contrib.auth.models import Group

class clinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = '__all__'
        labels = {
            'nombre' : 'Nombre de la Clínica',
            'telefono' : 'Telefono de la Clínica',
            #'responsables' : 'Responsable',
            'correo_electronico' : 'Correo Electrónico',
            'hora_inicio' : 'Hora de Apertura',
            'hora_fin' : 'Hora de Cierre',
            'numero_consultorios' : 'Número de Consultorios',
            'logo' : 'Logo de la Clínica'
        }
        widgets = {
            #'responsables': forms.Select(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'placeholder' : 'Ej: Clinica San Juan'}),
            'telefono': forms.TextInput(attrs={'placeholder' : '2411152829'}),
            'correo_electronico' : forms.TextInput(attrs={'placeholder' : 'Ej: correo@gmail.com'}),
            'direccion' : forms.TextInput(attrs={'placeholder' : 'Ej: Av. Tecnologico'}),
            'numero_consultorios': forms.NumberInput(attrs={'min': '1', 'placeholder' : '2'}),
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
