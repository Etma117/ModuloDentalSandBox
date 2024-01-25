import datetime
from xml.dom import ValidationErr
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'tipo_usuario', 'fecha_nacimiento', 'numero', 'clinicas',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'tipo_usuario', 'fecha_nacimiento', 'numero', 'clinicas',)


class CustomUserCreationFormTemplate(UserCreationForm):
    
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento:",
        widget=forms.DateInput(attrs={'type': 'text', 'id': 'date', 'placeholder': "DD/MM/YYYY"}),
        input_formats=['%d/%m/%Y'],
    )

    def clean_fechaNacimiento(self):
        data = self.cleaned_data['fecha_nacimiento']
        today = datetime.date.today()
        age = today.year - data.year - ((today.month, today.day) < (data.month, data.day))
        if age < 18:
            raise ValidationError('Debe de ser mayor de 18 años.')        
        if age > 110:
            raise ValidationError('La edad ingresada no es válida. Por favor, verifica la fecha de nacimiento.')
        return data
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'foto', 
                 'apellido_materno', 'direccion', 'celular', 'telefono_fijo', 
                 'sexo', 'fecha_nacimiento','clinicas',)  
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Seleccione la fecha de nacimiento', 'type': 'date'}),
            }
             
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationFormTemplate, self).__init__(*args, **kwargs)

       
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido Paterno'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['apellido_materno'].widget.attrs['placeholder'] = 'Apellido Materno'
        self.fields['last_name'].label = 'Apellido Paterno'
        self.fields['apellido_materno'].label = 'Apellido Materno'
        self.fields['direccion'].widget.attrs['placeholder'] = 'Ej. Av Moctezuma'
        self.fields['celular'].widget.attrs['placeholder'] = 'Numero de Celular'
        self.fields['telefono_fijo'].widget.attrs['placeholder'] = 'Numero de Teléfono'
        
        self.fields['sexo'].widget.attrs['placeholder'] = 'Sexo'
        self.fields['sexo'].label = 'Sexo'
        self.fields['clinicas'].widget.attrs['class'] = 'select2'


        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field and isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({'class': 'form-control'})


class CustomUserUpdateDentistaFormTemplate(UserChangeForm):
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento:",
        widget=forms.DateInput(attrs={'type': 'text', 'id': 'date', 'placeholder': "DD/MM/YYYY"}),
        input_formats=['%d/%m/%Y'],
     )

    def clean_fecha_nacimiento(self):
        data = self.cleaned_data['fecha_nacimiento']
        if data:  # Asegúrate de que la fecha de nacimiento no sea None
            today = datetime.date.today()
            age = today.year - data.year - ((today.month, today.day) < (data.month, data.day))
            if age < 18:
                raise ValidationErr('Debe de ser mayor de 18 años.')        
            if age > 110:
                raise ValidationErr('La edad ingresada no es válida. Por favor, verifica la fecha de nacimiento.')
        return data

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'foto', 
                  'apellido_materno', 'direccion', 'celular', 'telefono_fijo', 
                  'sexo', 'fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Seleccione la fecha de nacimiento'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateDentistaFormTemplate, self).__init__(*args, **kwargs)


        del self.fields['password']