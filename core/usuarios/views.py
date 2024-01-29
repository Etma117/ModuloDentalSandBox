# Django imports
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Local imports
from .models import CustomUser
from .forms import CustomUserCreationFormTemplate, CustomUserUpdateDentistaFormTemplate

# Create your views here.

class UserCreateViewDentista(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormTemplate
    template_name = 'register/register_user_dentista.html'
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
        context['navbar'] = 'gestion_usuarios'  # Cambia esto según la página activa
        context['seccion'] = 'ver_dentistas'  # Cambia esto según la página activa

        return context
    

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateDentistaFormTemplate  
    template_name = 'editar/edit_user_profile.html'  
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        messages.success(self.request, "Perfil actualizado con éxito.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'  # Cambia esto según la página activa
        context['seccion'] = 'editar_perfil'  # Cambia esto según la página activa
        return context
    

    def post(self, request, *args, **kwargs):
        if "change_password" in request.POST:
            return self.change_password(request)
        return super().post(request, *args, **kwargs)

    def change_password(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para no desloguear al usuario
            return JsonResponse({"success": True, "message": "Contraseña actualizada correctamente."})
        else:
            return JsonResponse({"success": False, "errors": form.errors})



    
class UserCreateViewPaciente(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormTemplate
    template_name = 'register/register_user_paciente.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.created_by = self.request.user
        user.save()
        admin_group, created = Group.objects.get_or_create(name='Paciente')
        user.groups.add(admin_group)
        messages.success(self.request, "Usuario creado con éxito.")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'  
        context['seccion'] = 'ver_pacientes' 

        return context
    

class UserCreateViewAsistente(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormTemplate
    template_name = 'register/register_user_asistente.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.created_by = self.request.user
        user.save()
        admin_group, created = Group.objects.get_or_create(name='Asistente')
        user.groups.add(admin_group)
        messages.success(self.request, "Usuario creado con éxito.")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios' 
        context['seccion'] = 'ver_asistente' 

        return context
    

class UserCreateViewResponsable(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormTemplate
    template_name = 'register/register_user_responsable.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.tipo_usuario = 'responsable'  
        user.created_by = self.request.user
        user.save()
        admin_group, created = Group.objects.get_or_create(name='Responsable')
        user.groups.add(admin_group)

        messages.success(self.request, "Usuario Responsable creado con éxito.")
        return super().form_valid(form)
    

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios' 
        context['seccion'] = 'ver_responsable' 

        return context
    
    
