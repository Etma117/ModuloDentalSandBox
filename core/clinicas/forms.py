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
            'hora_inicio': 'Hora de inicio',
            'hora_fin': 'Hora de fin',
            'correo_electronico': 'Correo electrónico',
            'equipamiento': 'Equipamiento',
            'numero_consultorios': 'Número de consultorios',
            # No se modifica 'responsables' según tu instrucción.
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo de la clínica'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección de la clínica'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Número de contacto'}),
            'hora_inicio': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'ejemplo@clinica.com'}),
            'equipamiento': forms.TextInput(attrs={'placeholder': 'Descripción del equipamiento'}),
            'numero_consultorios': forms.NumberInput(attrs={'placeholder': 'Cantidad de consultorios'}),
            # El campo 'logo' no necesita placeholder ya que será un campo de carga de archivo.
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            responsables_group = Group.objects.get(name='Responsable')
            self.fields['responsables'].queryset = CustomUser.objects.filter(groups=responsables_group)
        except Group.DoesNotExist:
            # Si el grupo 'Responsable' no existe, se asigna un queryset vacío
            self.fields['responsables'].queryset = CustomUser.objects.none()

        self.fields['responsables'].widget.attrs['class'] = 'select2'