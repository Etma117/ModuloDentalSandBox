from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from clinicas.models import Clinica
from usuarios.models import CustomUser
from django.shortcuts import redirect
from django.urls import reverse
from agenda.models import Cita
from django.db.models import Q

#Importamos los decoradores para crear que cada vista tenga su login required 
from django.http import JsonResponse

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login

from usuarios.models import CustomUser
from .forms import UserRecoveryForm


from django.contrib.auth.decorators import login_required

# Create your views here.

class home(LoginRequiredMixin, ListView):
    model= Cita
    context_object_name = 'citas'    
    template_name = 'menu.html'

    def get_queryset(self):
        # Obtener el usuario que inició sesión
        usuario_actual = self.request.user
        citas_aprobadas = Cita.objects.filter(
        Q(dentista=usuario_actual) | Q(paciente=usuario_actual),
        estado_cita='Aprobada'
        ).order_by('start')

        return citas_aprobadas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_clinicas'] = Clinica.objects.count()
        context['total_dentistas'] = CustomUser.objects.filter(tipo_usuario="dentista").count()
        context['total_responsables'] = CustomUser.objects.filter(tipo_usuario="responsable").count()
        context['total_pacientes'] = CustomUser.objects.filter(tipo_usuario="paciente").count()
        context['navbar'] = 'home' 

        usuario_conectado = self.request.user
        if usuario_conectado.tipo_usuario == 'responsable':
            clinicas_responsable = usuario_conectado.contar_clinicas_asignadas()
            context['clinicas_responsable'] = clinicas_responsable

        return context


def exit(request):
    logout(request)
    return redirect('homePage')

class homePageView(TemplateView):
    template_name= 'homepage/index.html'


class homePageViewChildren(TemplateView):
    template_name= 'homepage/indexChildren.html'

def recover_password(request):
    if request.method == 'POST':
        form = UserRecoveryForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            try:
                user = CustomUser.objects.get(username=username)
                # Renderizar las preguntas de seguridad para el usuario con un nuevo formulario
                # Aquí puedes optar por enviar las preguntas y construir un formulario en el frontend,
                # o renderizar un nuevo template con las preguntas de seguridad.
                return JsonResponse({
                    'success': True,
                    'pregunta_seguridad_1': user.get_pregunta_seguridad_1_display(),
                    'pregunta_seguridad_2': user.get_pregunta_seguridad_2_display(),
                })
            except CustomUser.DoesNotExist:
                # Manejar el error de que el usuario no existe
                return JsonResponse({'error': True, 'message': 'El usuario no existe.'})
    else:
        form = UserRecoveryForm()
    return render(request, 'recovery/recuperar_contraseña.html', {'form': form})


User = get_user_model()

def verify_security_answers(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        answer_1 = request.POST.get('security_answer_1')
        answer_2 = request.POST.get('security_answer_2')

        try:
            user = User.objects.get(username=username)
            # Comprobar si las respuestas proporcionadas coinciden con las almacenadas
            if user.respuesta_seguridad_1 == answer_1 and user.respuesta_seguridad_2 == answer_2:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': True, 'message': 'Respuestas de seguridad incorrectas.'})
        except User.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'El usuario no existe.'})


def set_new_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 and new_password1 == new_password2:
            try:
                user = User.objects.get(username=username)
                user.set_password(new_password1)
                user.save()
                return JsonResponse({'success': True, 'message': 'Contraseña actualizada correctamente.'})
            except User.DoesNotExist:
                return JsonResponse({'error': True, 'message': 'Usuario no encontrado.'})
        else:
            return JsonResponse({'error': True, 'message': 'Las contraseñas no coinciden o están vacías.'})
        

# Plantilla de denegado 

class templeteDenegado(TemplateView):
    template_name = 'denegado/denied.html'


def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')  # O el nombre de la URL del menú
    else:
        return redirect(reverse('account_login'))  
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='paciente').exists():
                return redirect('vista_paciente')
            else:
                return redirect('vista_normal')
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

@login_required
def vista_normal(request):
    return render(request, 'vista_normal.html')

@login_required
def vista_paciente(request):
    return render(request, 'vista_paciente.html')