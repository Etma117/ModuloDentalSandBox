from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

#Importamos los decoradores para crear que cada vista tenga su login required 
from django.http import JsonResponse

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login

from usuarios.models import CustomUser
from .forms import UserRecoveryForm

# Create your views here.

class home(LoginRequiredMixin, TemplateView):
    template_name = 'menu.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'home'  
        return context


def exit(request):
    logout(request)
    return redirect('home')




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
