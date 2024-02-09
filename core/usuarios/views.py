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
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from clinicas.models import Clinica
from core import settings
from django.views.decorators.http import require_POST

# Local imports
from .models import CustomUser
from .forms import CustomUserCreationAsistenteFormTemplate, CustomUserCreationFormDentista, CustomUserCreationFormTemplate, CustomUserUpdateDentistaFormTemplate
from django.views.generic import TemplateView
# Create your views here.


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class UserCreateViewDentista(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormDentista
    template_name = 'register/register_user_dentista.html'
    success_url = reverse_lazy('home') 


    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador','Responsable']).exists()
    

    def form_valid(self, form):
        user = form.save(commit=False)
        user.created_by = self.request.user
        user.tipo_usuario = 'dentista'  

        user.save()
        admin_group, created = Group.objects.get_or_create(name='Dentista')
        user.groups.add(admin_group)
        messages.success(self.request, "Usuario creado con éxito.")
        return super().form_valid(form)
    
 
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        else:
            return redirect('denegado')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # Llamada correcta a super()
        kwargs['current_user'] = self.request.user  # Añade el usuario actual a los argumentos del formulario
        return kwargs

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
        
        user = self.request.user
        preguntas_configuradas = user.pregunta_seguridad_1 and user.pregunta_seguridad_2
        context['preguntas_configuradas'] = preguntas_configuradas
        context['preguntas_seguridad_1'] = CustomUser.PREGUNTAS_SEGURIDAD_1
        context['preguntas_seguridad_2'] = CustomUser.PREGUNTAS_SEGURIDAD_2

        return context
    

    def post(self, request, *args, **kwargs):
        if "change_password" in request.POST:
            return self.change_password(request)
        elif "update_security_questions" in request.POST:
            return self.update_security_questions(request)
        return super().post(request, *args, **kwargs)
    
    def update_security_questions(self, request):
        pregunta_1 = request.POST.get('pregunta_seguridad_1')
        respuesta_1 = request.POST.get('respuesta_seguridad_1')
        pregunta_2 = request.POST.get('pregunta_seguridad_2')
        respuesta_2 = request.POST.get('respuesta_seguridad_2')

        if not all([pregunta_1, respuesta_1, pregunta_2, respuesta_2]):
            # Si alguna pregunta o respuesta está vacía, enviar un error
            return JsonResponse({"error": False, "message": "Todas las preguntas y respuestas de seguridad son obligatorias."})

        # Si todas las preguntas y respuestas están presentes, proceder a guardarlas
        user = self.request.user
        user.pregunta_seguridad_1 = pregunta_1
        user.respuesta_seguridad_1 = respuesta_1
        user.pregunta_seguridad_2 = pregunta_2
        user.respuesta_seguridad_2 = respuesta_2
        user.save()

        return JsonResponse({"success": True, "message": "Preguntas de seguridad actualizadas correctamente."})

    def change_password(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para no desloguear al usuario
            return JsonResponse({"success": True, "message": "Contraseña actualizada correctamente."})
        else:
            # Recopila los mensajes de error del formulario y los envía al frontend
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({"success": False, "errors": errors})

    
class UserCreateViewPaciente(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormDentista
    template_name = 'register/register_user_paciente.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.created_by = self.request.user
        user.tipo_usuario = 'paciente'  

        user.save()
        admin_group, created = Group.objects.get_or_create(name='Paciente')
        user.groups.add(admin_group)
        messages.success(self.request, "Usuario creado con éxito.")
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # Llamada correcta a super()
        kwargs['current_user'] = self.request.user  # Añade el usuario actual a los argumentos del formulario
        return kwargs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'  
        context['seccion'] = 'ver_pacientes' 

        return context
    

class UserCreateViewAsistente(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormDentista
    template_name = 'register/register_user_asistente.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.tipo_usuario = 'asistente'  

        user.created_by = self.request.user
        user.save()
        admin_group, created = Group.objects.get_or_create(name='Asistente')
        user.groups.add(admin_group)
        messages.success(self.request, "Usuario creado con éxito.")
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # Llamada correcta a super()
        kwargs['current_user'] = self.request.user  # Añade el usuario actual a los argumentos del formulario
        return kwargs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios' 
        context['seccion'] = 'ver_asistente' 

        return context
    

class UserCreateViewResponsable(CreateView):
    model = CustomUser
    form_class = CustomUserCreationFormDentista
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
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # Llamada correcta a super()
        kwargs['current_user'] = self.request.user  # Añade el usuario actual a los argumentos del formulario
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios' 
        context['seccion'] = 'ver_responsable' 

        return context
    
    
# lista de usuarios 
from django.db.models import Count, Case, When, Value
from django.db import models  # Asegúrate de añadir esta línea al inicio de tu archivo

class ResponsableListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'listas/listResponsable.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'responsables'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()
    
    def get_queryset(self):
        try:
            paciente_group = Group.objects.get(name='Responsable')
            # Filtra usuarios en el grupo 'Responsable'
            queryset = CustomUser.objects.filter(groups=paciente_group).annotate(
                num_clinicas=Count('clinicas'),
                # Añade un campo 'has_clinica' que es falso si el número de clínicas es 0 (indicando que no tiene clínicas)
                has_clinica=Case(
                    When(num_clinicas=0, then=Value(False)),
                    default=Value(True),
                    output_field=models.BooleanField(),
                )
            ).order_by('has_clinica', 'first_name')  # Ordena primero por 'has_clinica' y luego por 'first_name'
            return queryset
        except Group.DoesNotExist:
            return CustomUser.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_responsable'
        context['grupo_responsable_existe'] = Group.objects.filter(name='Responsable').exists()
        return context

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        else:
            return redirect('denegado')
class PacienteListView(ListView):
    model = CustomUser
    template_name = 'listas/listPacientes.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'pacientes'

    def get_queryset(self):
        try:
            # Intentar obtener el grupo "Paciente"
            paciente_group = Group.objects.get(name='Paciente')
            # Filtrar usuarios que pertenecen al grupo "Paciente"
            return CustomUser.objects.filter(groups=paciente_group)
        except Group.DoesNotExist:
            # Si no existe el grupo, devolver un queryset vacío
            return CustomUser.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_pacientes'
        context['grupo_paciente_existe'] = Group.objects.filter(name='Paciente').exists()
        return context
    

class DentistaListView(ListView):
    model = CustomUser
    template_name = 'listas/listDentistas.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'dentistas'

    def get_queryset(self):
        try:
            paciente_group = Group.objects.get(name='Dentista')
            return CustomUser.objects.filter(groups=paciente_group)
        except Group.DoesNotExist:
            # Si no existe el grupo, devolver un queryset vacío
            return CustomUser.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_dentistas'
        context['grupo_dentista_existe'] = Group.objects.filter(name='Dentista').exists()

        return context
    
class AsistenteListView(ListView):
    model = CustomUser
    template_name = 'listas/listAsistentes.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'asistentes'

    def get_queryset(self):
        try:
            paciente_group = Group.objects.get(name='Asistente')
            return CustomUser.objects.filter(groups=paciente_group)
        except Group.DoesNotExist:
            # Si no existe el grupo, devolver un queryset vacío
            return CustomUser.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_asistente'
        context['grupo_asistente_existe'] = Group.objects.filter(name='Asistente').exists()

        return context
    




# Detalles del paciente 

class PacienteDetailView(DetailView):
    model = CustomUser
    template_name = 'detalles/detallePaciente.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'paciente'

    def get_object(self, queryset=None):
        # Obtén el paciente por su id
        paciente_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, id=paciente_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_pacientes'
        
        return context
    
class AsistenteDetailView(DetailView):
    model = CustomUser
    template_name = 'detalles/detalleAsistente.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'paciente'

    def get_object(self, queryset=None):
        # Obtén el paciente por su id
        paciente_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, id=paciente_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_asistente'
        return context
    
class DentistaDetailView(DetailView):
    model = CustomUser
    template_name = 'detalles/detalleDentista.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'paciente'

    def get_object(self, queryset=None):
        # Obtén el paciente por su id
        paciente_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, id=paciente_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_asistente'
        return context
    

class ResponsableDetailView(DetailView):
    model = CustomUser
    template_name = 'detalles/detalleResponsable.html'  # Actualiza con tu ruta de plantilla
    context_object_name = 'paciente'

    def get_object(self, queryset=None):
        # Obtén el paciente por su id
        paciente_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, id=paciente_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'gestion_usuarios'
        context['seccion'] = 'ver_responsable'
     
        # Obtén el paciente actual
        paciente = self.get_object()
        
        # Obtén las clínicas que NO están asociadas con el paciente
        clinicas_no_asociadas = Clinica.objects.exclude(id__in=paciente.clinicas.all())
        
        context['clinicas'] = clinicas_no_asociadas
        return context
    
@login_required
def eliminar_relacion_clinica(request, user_id, clinica_id):
    usuario = get_object_or_404(CustomUser, id=user_id)
    clinica = get_object_or_404(Clinica, id=clinica_id)
    if request.method == "POST":
        usuario.clinicas.remove(clinica)
        messages.success(request, 'Relación con clínica removida con éxito.')
        return HttpResponseRedirect(reverse('responsable_detail', args=[usuario.id]))
    else:
        # Si el método no es POST, redirige a la vista de detalle usando 'pk'
        return redirect('responsable_detail', pk=usuario.id)

@login_required
@require_POST  # Asegura que esta vista solo se pueda acceder mediante una solicitud POST.
def agregar_clinica_a_usuario(request, user_id):
    usuario = get_object_or_404(CustomUser, id=user_id)
    clinicas_ids = request.POST.getlist('clinicas')  # 'clinicas' es el nombre del campo <select> en tu formulario HTML.

    for clinica_id in clinicas_ids:
        clinica = get_object_or_404(Clinica, id=clinica_id)
        usuario.clinicas.add(clinica)

    messages.success(request, 'Clínicas añadidas con éxito.')
    return redirect('responsable_detail', pk=usuario.id)


class verOdontograma(TemplateView):
    template_name = 'detalles/odontograma.html'