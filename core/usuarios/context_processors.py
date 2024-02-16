


import datetime
from django.utils import timezone

from usuarios.models import CustomUser
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import logout
from datetime import timedelta

def profile_completion(request):
    user_profile_complete = True  # Cambiar por la lógica real de comprobación
    if request.user.is_authenticated:
        user_profile_complete = request.user.profile_complete()
    return {'user_profile_complete': user_profile_complete}


# Agregar un clasificador de grupos 

def user_groups(request):
    groups = [group.name for group in request.user.groups.all()]
    return {'user_groups': groups}



def group_context(request):

    context = {
        'es_dentista': request.user.groups.filter(name='Dentista').exists(),
        'es_paciente': request.user.groups.filter(name='Paciente').exists(),
        'es_responsable': request.user.groups.filter(name='Responsable').exists(),
        'es_asistente': request.user.groups.filter(name='Asistente').exists(),
        'es_administrador': request.user.groups.filter(name='Administrador').exists(),
        'es_superusuario': request.user.is_superuser,  # Verificación para superusuario

    }
    return context

def user_profile_picture(request):
    if request.user.is_authenticated:
        # Obtiene el nombre y apellidos del usuario
        nombre = request.user.first_name
        apellido = request.user.last_name
        sexo = request.user.sexo  # Asumiendo que el campo sexo es parte del modelo de usuario.
        sexo_display = dict(CustomUser.SEX_CHOICES).get(sexo, '')

        return {
            'user_id': request.user.id,
            'user_picture': request.user.foto.url if request.user.foto else None,
            'user_nombre': nombre,
            'user_apellido': apellido,
            'user_sexo': sexo_display,  # Agregamos esta línea.

            # ... puedes agregar más información del usuario aquí si es necesario ...
        }
    return {}


def current_time(request):
    return {
        'current_time': timezone.localtime()
    }



