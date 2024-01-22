from django.shortcuts import render

from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import CustomUser
from .forms import CustomUserCreationFormTemplate
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

class UserCreateViewDentista(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormTemplate
    template_name = 'register_user_dentista.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.created_by = self.request.user
        user.save()
        admin_group, created = Group.objects.get_or_create(name='Dentista')
        user.groups.add(admin_group)
        messages.success(self.request, "Usuario creado con éxito.")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_user'  # Cambia esto según la página activa
        context['seccion'] = 'ver_usuarios'  # Cambia esto según la página activa

        return context
    
