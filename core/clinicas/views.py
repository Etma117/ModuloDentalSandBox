from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from usuarios.models import CustomUser 
from .models import Clinica
from .forms import clinicaForm
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages

class Clinicas(ListView):
    model = Clinica
    template_name = 'clinicas.html'
    context_object_name = 'clinica'

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

class vistaClinica(DetailView):
    model = Clinica
    template_name = 'vistaClinicas.html'
    context_object_name = 'clinica'

class eliminarClinica(DeleteView):
    model = Clinica
    template_name = 'eliminarClinica.html'
    success_url = reverse_lazy('clinicas')

class editarClinica(UpdateView):
    model = Clinica
    template_name = 'nuevaClinica.html'
    form_class = clinicaForm
    context_object_name = 'clinica'
    success_url = reverse_lazy('clinicas')