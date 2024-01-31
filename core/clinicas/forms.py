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
            'telefono' : 'Telefono de la Clínica'
        }
        widgets = {
            'responsables': forms.Select(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        responsables_group = Group.objects.get(name='Responsable')
        self.fields['responsables'].queryset = CustomUser.objects.filter(groups=responsables_group)
