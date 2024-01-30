


from django.urls import path
from usuarios.views import AsistenteListView, DentistaListView, PacienteListView, UserCreateViewAsistente, UserCreateViewDentista, UserCreateViewPaciente, UserCreateViewResponsable, UserUpdateView,ResponsableListView

urlpatterns = [
    path('registrar-usuario-dentista/', UserCreateViewDentista.as_view(), name='register_user_dentista'),
    path('registrar-usuario-paciente/', UserCreateViewPaciente.as_view(), name='UserCreateViewPaciente'),
    path('registrar-usuario-asistente/', UserCreateViewAsistente.as_view(), name='UserCreateViewAsistente'),
    path('registrar-usuario-Responsable/', UserCreateViewResponsable.as_view(), name='UserCreateViewResponsable'),

    
    path('editar-usuario/<int:pk>/', UserUpdateView.as_view(), name='editar_usuario'),



    path('ver-responsable/', ResponsableListView.as_view(), name='ResponsableListView'),
    path('ver-pacientes/', PacienteListView.as_view(), name='ver_pacientes'),
    path('ver-asistentes/', AsistenteListView.as_view(), name='AsistenteListView'),
    path('ver-dentistas/', DentistaListView.as_view(), name='DentistaListView'),

]