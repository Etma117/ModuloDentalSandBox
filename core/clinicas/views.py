from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView 
from .models import Clinica
from .forms import clinicaForm
from django.urls import reverse_lazy

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

class vistaClinica(DetailView):
    template_name = 'vistaClinicas.html'

    def get(self, request, clinica_id, *args, **kwargs):
        clinica = Clinica.objects.get(id=clinica_id)
        return render(request, self.template_name, {'clinica': clinica})

class eliminarClinica(DeleteView):
    model = Clinica
    template_name = 'eliminarClinica.html'
    success_url = reverse_lazy('clinicas')

class editarClinica(UpdateView):
    model = Clinica
    template_name = 'editarClinica.html'
    form_class = clinicaForm
    context_object_name = 'clinica'
    success_url = reverse_lazy('clinicas')