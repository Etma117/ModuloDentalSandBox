from django import forms
from agenda.models import Cita  


class CitasFormP(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        # widgets = {
        #     'motivo': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'required': True}),
        #     'municipio': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'required': True}),
        #     'clinica': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'required': True}),
        #     'dentista': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'required': True}),
        #     'fecha': forms.DateInput(attrs={'class': 'form-control mb-3', 'required': True}),
        #     'horario': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'required': True}),
        # }