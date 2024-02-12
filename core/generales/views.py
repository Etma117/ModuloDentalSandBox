from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from agenda.models import Cita

#Importamos los decoradores para crear que cada vista tenga su login required 

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

class home(LoginRequiredMixin, TemplateView):
    model= Cita
    context_object_name = 'citas'    
    template_name = 'menu.html'
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'home'  
        return context


def exit(request):
    logout(request)
    return redirect('home')
