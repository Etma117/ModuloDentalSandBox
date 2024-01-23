


from django.urls import path
from usuarios.views import UserCreateViewAsistente, UserCreateViewDentista, UserCreateViewPaciente

urlpatterns = [
    path('registrar-usuario-dentista/', UserCreateViewDentista.as_view(), name='register_user_dentista'),
    path('registrar-usuario-paciente/', UserCreateViewPaciente.as_view(), name='UserCreateViewPaciente'),
    path('registrar-usuario-asistente/', UserCreateViewAsistente.as_view(), name='UserCreateViewAsistente'),


]