from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from usuarios.models import CustomUser 
from .models import Clinica
from .forms import ClinicaForm

from agenda.models import DiasNoLaborablesCalendar


class Clinicas(ListView):
    model = Clinica
    template_name = 'clinicas.html'
    context_object_name = 'clinica'

class ClinicaCrear(CreateView):
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

            # Crea o recupera un calendario para la clínica
            slug_prefix = "dias_no_laborables_clinica_"
            dias_no_laborables_calendar = DiasNoLaborablesCalendar.objects.filter(slug=f"{slug_prefix}{self.object.id}").first()

            if not dias_no_laborables_calendar:
                new_calendar = DiasNoLaborablesCalendar.objects.create(
                    name=f"Días No Laborables - {self.object.nombre}",
                    slug=f"{slug_prefix}{self.object.id}",
                    clinica=self.object
                )
            else:
                user.calendar_id = dias_no_laborables_calendar.id
                user.save()

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
    form_class = ClinicaForm
    context_object_name = 'clinica'
    success_url = reverse_lazy('clinicas')