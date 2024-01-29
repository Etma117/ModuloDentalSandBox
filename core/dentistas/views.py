from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import Group

from usuarios.models import CustomUser

# Create your views here.


class DentistaListView(ListView):
    model = CustomUser
    template_name = 'listDentistas.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'dentistas'

    def get_queryset(self):
        try:
            paciente_group = Group.objects.get(name='Dentista')
            return CustomUser.objects.filter(groups=paciente_group)
        except Group.DoesNotExist:
            # Si no existe el grupo, devolver un queryset vacío
            return CustomUser.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_dentistas'
        context['grupo_dentista_existe'] = Group.objects.filter(name='Dentista').exists()

        return context