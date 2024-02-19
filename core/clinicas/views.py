from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView 
from .models import Clinica
from .forms import clinicaForm
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from usuarios.models import CustomUser

class Clinicas(ListView):
    model = Clinica
    template_name = 'clinicas.html'
    context_object_name = 'clinica'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            usuario_actual = self.request.user
            if usuario_actual.tipo_usuario == 'responsable':
                return usuario_actual.clinicas.all()
            elif usuario_actual.tipo_usuario == 'administrador':
                return Clinica.objects.all()
        return Clinica.objects.none()

class clinicaCrear(CreateView):
    model = Clinica
    template_name = 'nuevaClinica.html'
    form_class = clinicaForm
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

    def get(self, request, pk, *args, **kwargs):
        clinica = Clinica.objects.get(id=pk)
        return render(request, self.template_name, {'clinica': clinica})

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
    form_class = clinicaForm
    context_object_name = 'clinica'
    success_url = reverse_lazy('clinicas')