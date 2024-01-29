from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import Group

from usuarios.models import CustomUser

# Create your views here.



class PacienteListView(ListView):
    model = CustomUser
    template_name = 'listPacientes.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'pacientes'

    def get_queryset(self):
        # Obtener el grupo "Paciente"
        paciente_group = Group.objects.get(name='Paciente')
        # Filtrar usuarios que pertenecen al grupo "Paciente"
        return CustomUser.objects.filter(groups=paciente_group)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_pacientes'
        return context
    