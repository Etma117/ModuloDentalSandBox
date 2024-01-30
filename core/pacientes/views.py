from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import Group
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404


from usuarios.models import CustomUser

# Create your views here.



class PacienteListView(ListView):
    model = CustomUser
    template_name = 'listPacientes.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'pacientes'

    def get_queryset(self):
        try:
            # Intentar obtener el grupo "Paciente"
            paciente_group = Group.objects.get(name='Paciente')
            # Filtrar usuarios que pertenecen al grupo "Paciente"
            return CustomUser.objects.filter(groups=paciente_group)
        except Group.DoesNotExist:
            # Si no existe el grupo, devolver un queryset vacío
            return CustomUser.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_pacientes'
        return context
    
class PacienteDetailView(DetailView):
    model = CustomUser
    template_name = 'detallepaciente.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'paciente'

    def get_object(self, queryset=None):
        # Obtén el paciente por su id
        paciente_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, id=paciente_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_pacientes'
        return context