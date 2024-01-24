


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
        'es_administrador': request.user.groups.filter(name='Administrador').exists()
    }
    return context