


from django.urls import path
from usuarios.views import UserCreateViewAsistente, UserCreateViewDentista, UserCreateViewPaciente, UserCreateViewResponsable

urlpatterns = [
    path('registrar-usuario-dentista/', UserCreateViewDentista.as_view(), name='register_user_dentista'),
    path('registrar-usuario-paciente/', UserCreateViewPaciente.as_view(), name='UserCreateViewPaciente'),
    path('registrar-usuario-asistente/', UserCreateViewAsistente.as_view(), name='UserCreateViewAsistente'),
    path('registrar-usuario-Responsable/', UserCreateViewResponsable.as_view(), name='UserCreateViewResponsable'),


]