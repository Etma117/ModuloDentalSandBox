from django.urls import path
from . import views
from .views import agregar_clinica_a_dentista, agregar_clinica_a_responsable, clinicaCrear, Clinicas, eliminar_relacion_dentista_clinica, eliminar_relacion_responsable_clinica, vistaClinica, eliminarClinica, editarClinica

urlpatterns = [
    path('ver-clinicas/', Clinicas.as_view(), name='clinicas'),
    path('detalle-clinica/<int:pk>', vistaClinica.as_view(), name='vistaClinicas'),
    path('crear-clinica/', clinicaCrear.as_view(), name='nuevaClinica'),
    path('eliminar-clinica/<int:pk>', eliminarClinica.as_view(), name='eliminarClinica'),
    path('editar-clinica/<int:pk>', editarClinica.as_view(), name='editarClinica'),

    # ELIMINAR RELACION Y AGREGAR RELACION CON RESPONSABLE
    path('eliminar-relacion-clinica-responsable/<int:user_id>/<int:clinica_id>/', eliminar_relacion_responsable_clinica, name='eliminar_relacion_responsable'),
    path('agregar-relacion-responsable/<int:clinica_id>/', agregar_clinica_a_responsable, name='agregar_clinica_a_responsable'),
    # ELIMINAR RELACION Y AGREGAR RELACION CON DENTISTA
    path('eliminar-relacion-clinica-dentista/<int:user_id>/<int:clinica_id>/', eliminar_relacion_dentista_clinica, name='eliminar_relacion_clinica_dentista'),
    path('agregar-relacion-dentista-clinica/<int:clinica_id>/', agregar_clinica_a_dentista, name='agregar_clinica_a_dentista'),



]

