import datetime
from xml.dom import ValidationErr
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator
from django.contrib.auth.forms import PasswordChangeForm
from clinicas.models import Clinica
from .models import AsistenteDentista
from django.forms import inlineformset_factory


class CustomPasswordChangeForm(PasswordChangeForm):
    pass  # Personaliza si es necesario


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


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'foto', 
                 'apellido_materno', 'direccion', 'celular', 'telefono_fijo', 
                 'sexo', 'fecha_nacimiento','clinicas',)  
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Seleccione la fecha de nacimiento', 'type': 'date'}),
            'sexo': forms.Select(attrs={'placeholder': 'Sexo'}),

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

        self.fields['clinicas'].widget.attrs['class'] = 'select2'

        campos_no_requeridos = ['telefono_fijo', 'foto']
        for field_name in self.fields:
            if field_name in campos_no_requeridos:
                self.fields[field_name].required = False
            else:
                self.fields[field_name].required = True

        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field and isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({'class': 'form-control'})

class CustomUserCreationAsistenteFormTemplate(UserCreationForm):
    
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento:",
        widget=forms.DateInput(attrs={'type': 'text', 'id': 'date', 'placeholder': "DD/MM/YYYY"}),
        input_formats=['%d/%m/%Y'],
    )


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'foto', 
                 'apellido_materno', 'direccion', 'celular', 'telefono_fijo', 
                 'sexo', 'fecha_nacimiento','clinicas',)  
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Seleccione la fecha de nacimiento', 'type': 'date'}),
            'sexo': forms.Select(attrs={'placeholder': 'Sexo'}),

            }
             
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationAsistenteFormTemplate, self).__init__(*args, **kwargs)

       
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

        self.fields['clinicas'].widget.attrs['class'] = 'select2'

        campos_no_requeridos = ['telefono_fijo', 'foto']
        for field_name in self.fields:
            if field_name in campos_no_requeridos:
                self.fields[field_name].required = False
            else:
                self.fields[field_name].required = True

        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field and isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({'class': 'form-control'})

AsistenteDentistaFormSet = inlineformset_factory(
    CustomUser, 
    AsistenteDentista, 
    fields=('dentista',), 
    extra=1, 
    can_delete=True,
    fk_name='asistente'  # Especifica que se utilizará la clave foránea 'asistente'
)


class CustomUserCreationFormDentista(UserCreationForm):
    
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento:",
        widget=forms.DateInput(attrs={'type': 'text', 'id': 'date', 'placeholder': "DD/MM/YYYY"}),
        input_formats=['%d/%m/%Y'],
    )


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'foto', 
                 'apellido_materno', 'direccion', 'celular', 'telefono_fijo', 
                 'sexo', 'fecha_nacimiento','clinicas',)  
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'Seleccione la fecha de nacimiento', 'type': 'date'}),
            'sexo': forms.Select(attrs={'placeholder': 'Sexo'}),

            }
             
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)

        super(CustomUserCreationFormDentista, self).__init__(*args, **kwargs)
        if current_user is not None:
            if current_user.is_superuser or current_user.groups.filter(name='Administrador').exists():
                # Si el usuario es superusuario o del grupo Administrador, muestra todas las clínicas
                self.fields['clinicas'].queryset = Clinica.objects.all()
            else:
                # De lo contrario, filtra las clínicas basadas en las asignadas al usuario
                self.fields['clinicas'].queryset = current_user.clinicas.all()


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

        self.fields['clinicas'].widget.attrs['class'] = 'select2'

        campos_no_requeridos = ['telefono_fijo', 'foto']
        for field_name in self.fields:
            if field_name in campos_no_requeridos:
                self.fields[field_name].required = False
            else:
                self.fields[field_name].required = True

        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field and isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({'class': 'form-control'})

class CustomUserUpdateDentistaFormTemplate(UserChangeForm):
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento:",
        widget=forms.DateInput(attrs={'type': 'text', 'id': 'date', 'placeholder': "DD/MM/YYYY"}),
        input_formats=['%d/%m/%Y'],
    )

    last_name = forms.CharField(
        label="Apellido paterno:",
        widget=forms.TextInput(attrs={'placeholder': "Apellido Paterno", 'class': 'alguna-clase'}),
    )

    celular = forms.CharField(
        label="No. celular:",
        widget=forms.TextInput(),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'foto', 
                  'apellido_materno', 'direccion', 'celular', 'telefono_fijo', 
                  'sexo', 'fecha_nacimiento')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido paterno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'apellido_materno': forms.TextInput(attrs={'placeholder': 'Apellido Materno'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Celular'}),
            'telefono_fijo': forms.TextInput(attrs={'placeholder': 'Teléfono Fijo'}),
            'sexo': forms.Select(attrs={'placeholder': 'Sexo'}),
            # 'fecha_nacimiento' ya está definido arriba
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateDentistaFormTemplate, self).__init__(*args, **kwargs)
        del self.fields['password']

    def clean_fecha_nacimiento(self):
        data = self.cleaned_data['fecha_nacimiento']
        if data:
            today = datetime.date.today()
            age = today.year - data.year - ((today.month, today.day) < (data.month, data.day))
            if age < 18:
                raise forms.ValidationError('Debe de ser mayor de 18 años.')
            if age > 110:
                raise forms.ValidationError('La edad ingresada no es válida. Por favor, verifica la fecha de nacimiento.')
        return data




class CustomUserCreationForm(forms.ModelForm):
    # Tus otros campos...

    pregunta_seguridad_1 = forms.ChoiceField(choices=CustomUser.PREGUNTAS_SEGURIDAD_1, required=True)
    respuesta_seguridad_1 = forms.CharField(widget=forms.PasswordInput, required=True)
    pregunta_seguridad_2 = forms.ChoiceField(choices=CustomUser.PREGUNTAS_SEGURIDAD_2, required=True)
    respuesta_seguridad_2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'pregunta_seguridad_1', 'respuesta_seguridad_1', 'pregunta_seguridad_2', 'respuesta_seguridad_2')


class UserRecoveryForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=150)