from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

#Importamos los decoradores para crear que cada vista tenga su login required 

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

class home(LoginRequiredMixin, TemplateView):
    template_name = 'menu.html'


    
def exit(request):
    logout(request)
    return redirect('home')
