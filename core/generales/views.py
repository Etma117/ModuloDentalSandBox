from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from clinicas.models import Clinica
from usuarios.models import CustomUser

#Importamos los decoradores para crear que cada vista tenga su login required 

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

class home(LoginRequiredMixin, TemplateView):
    template_name = 'menu.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_clinicas'] = Clinica.objects.count()
        context['total_dentistas'] = CustomUser.objects.filter(tipo_usuario="dentista").count()
        context['total_responsables'] = CustomUser.objects.filter(tipo_usuario="responsable").count()
        context['navbar'] = 'home'  
        return context


def exit(request):
    logout(request)
    return redirect('home')
