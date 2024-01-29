from django import forms
from .models import Clinica

class clinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = '__all__'
 