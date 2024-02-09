


from django.urls import path
from usuarios.views import AsistenteDetailView, AsistenteListView, DentistaDetailView, DentistaListView, PacienteDetailView, PacienteListView, ResponsableDetailView, UserCreateViewAsistente, UserCreateViewDentista, UserCreateViewPaciente, UserCreateViewResponsable, UserUpdateView,ResponsableListView, agregar_clinica_a_usuario, verOdontograma
from usuarios.views import eliminar_relacion_clinica
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


    # DETALLES DE USUARIOS
    path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('dentista/<int:pk>/', DentistaDetailView.as_view(), name='dentista_detail'),
    path('responsable/<int:pk>/', ResponsableDetailView.as_view(), name='responsable_detail'),
    path('asistente/<int:pk>/', AsistenteDetailView.as_view(), name='asistente_detail'),


    # ELIMINAR 

    path('usuario/<int:user_id>/eliminar-clinica/<int:clinica_id>/', eliminar_relacion_clinica, name='eliminar_relacion_clinica'),
    path('agregar-clinica/<int:user_id>/', agregar_clinica_a_usuario, name='agregar_clinica_responsable'),

    path('odontograma/', verOdontograma.as_view(), name="verOdontograma"),
]