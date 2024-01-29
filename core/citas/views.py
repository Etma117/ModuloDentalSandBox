from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Cita
from .forms import CitaForm

class CitaListar(LoginRequiredMixin, ListView):  #Lista de todas las citas
    model = Cita
    template_name = 'Citas.html' 
    context_object_name = 'cita'
    success_url = '/citas'

    
class CitaCrearView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView ): #Vista para agendar la cita
    model = Cita
    template_name = 'Agendar_Cita.html'
    context_object_name = 'cita'
    form_class = CitaForm    
    success_url = reverse_lazy('Citas')
    
    success_message = 'Cita agendada...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'citas.add_cita'
    raise_exception = True 


class CitaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): #Vista para los detalles de una cita especifica
    model = Cita 
    template_name = 'detalle_Cita.html'  
    context_object_name = 'cita'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'agenda.view_evento'
    raise_exception = True 


class CitaUpdateView (LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView): #Vista para actualizar la cita
    model=Cita
    template_name='Agendar_Cita.html'
    context_object_name= 'cita'
    form_class= CitaForm    
    success_url = reverse_lazy('Citas') #Nombre de la url, no la url en si

    success_message ='Cita modificada...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'citas.change_cita'
    raise_exception = True 

class CitaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView): #Vista para cancelar la cita
    model = Cita
    template_name = 'Cancelar_Cita.html'
    context_object_name = 'cita'
    success_url = reverse_lazy('Citas')
    
    success_message = 'Cita Cancelada...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'citas.delete_cita'
    raise_exception = True 