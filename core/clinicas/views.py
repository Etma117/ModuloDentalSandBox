from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView 
from .models import Clinica
from .forms import ClinicaForm
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from usuarios.models import CustomUser




#NOTA: CONSIDERAR PONER EL QUERYSET DE ADMINISTRADOR
class Clinicas(ListView):
    model = Clinica
    template_name = 'clinicas.html'
    context_object_name = 'clinica'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            usuario_actual = self.request.user
            # Verifica si el usuario es superusuario
            if usuario_actual.is_superuser:
                return Clinica.objects.all()
            elif usuario_actual.tipo_usuario == 'responsable':
                return usuario_actual.clinicas.all()
            elif usuario_actual.tipo_usuario == 'administrador':
                return Clinica.objects.all()
        return Clinica.objects.none()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_clinicas'
        context['seccion'] = 'ver_clinicas'
        return context

class clinicaCrear(CreateView):
    model = Clinica
    template_name = 'nuevaClinica.html'
    form_class = ClinicaForm
    context_object_name = 'clinica'
    success_url = reverse_lazy('clinicas')

    def form_valid(self, form):
        with transaction.atomic():
            # Guarda la instancia de Clinica directamente
            self.object = form.save()

            # Recupera y asigna los responsables como se describió anteriormente
            responsables_ids = self.request.POST.getlist('responsables')
            for user_id in responsables_ids:
                user = CustomUser.objects.get(id=user_id)
                user.clinicas.add(self.object)
            
        messages.success(self.request, 'La clínica ha sido creada con éxito.')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_clinicas'
        context['seccion'] = 'crear_clinicas'

        return context

class vistaClinica(DetailView):
    model = Clinica
    template_name = 'vistaClinicas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_clinicas'
        context['seccion'] = 'ver_clinicas'

        return context

class eliminarClinica(DeleteView):
    model = Clinica
    template_name = 'eliminarClinica.html'
    success_url = reverse_lazy('clinicas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_clinicas'
        context['seccion'] = 'ver_clinicas'

        return context
        
class editarClinica(UpdateView):
    model = Clinica
    template_name = 'editarClinica.html'
    form_class = ClinicaForm
    context_object_name = 'clinica'
    success_url = reverse_lazy('clinicas')

    def form_valid(self, form):
        clinica = self.object  # La instancia de la clínica que se está editando.
        nuevos_responsables_ids = [usuario.id for usuario in form.cleaned_data['responsables']]
        
        # Obtener los IDs de los responsables actuales para poder comparar después.
        actuales_responsables_ids = list(clinica.responsables.values_list('id', flat=True))
        
        # Identificar responsables a remover y a añadir.
        responsables_a_remover = set(actuales_responsables_ids) - set(nuevos_responsables_ids)
        responsables_a_añadir = set(nuevos_responsables_ids) - set(actuales_responsables_ids)
        
        # Remover las relaciones de los responsables que ya no están asociados a la clínica.
        for user_id in responsables_a_remover:
            usuario = CustomUser.objects.get(id=user_id)
            clinica.responsables.remove(usuario)
            usuario.clinicas.remove(clinica)
        
        # Añadir las nuevas relaciones para los nuevos responsables.
        for user_id in responsables_a_añadir:
            usuario = CustomUser.objects.get(id=user_id)
            clinica.responsables.add(usuario)
            usuario.clinicas.add(clinica)

        response = super().form_valid(form)
        messages.success(self.request, 'Clínica actualizada con éxito.')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_clinicas'
        context['seccion'] = 'ver_clinicas'

        return context
