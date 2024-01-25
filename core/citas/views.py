from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.views import View
from .models import Cita
from .forms import CitaForm

class CitaListar(ListView):
    model = Cita
    template_name = 'Citas.html' 
    context_object_name = 'cita'
    success_url = 'Citas'

    
class CitaCrearView(LoginRequiredMixin, SuccessMessageMixin, CreateView, PermissionRequiredMixin):
    model = Cita
    template_name = 'Agendar_Cita.html'
    context_object_name = 'cita'
    form_class = CitaForm
    success_url = 'Citas'
    
    success_message = 'Cita agendada...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'citas.add_cita'
    raise_exception = True 


class CitaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Cita
    template_name = 'detalle_Cita.html'  
    context_object_name = 'cita'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'agenda.view_evento'
    raise_exception = True 