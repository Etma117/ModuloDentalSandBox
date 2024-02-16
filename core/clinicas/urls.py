from django.urls import path
from . import views
from .views import clinicaCrear, Clinicas, vistaClinica, eliminarClinica, editarClinica

urlpatterns = [
    path('ver-clinicas/', Clinicas.as_view(), name='clinicas'),
    path('detalle-clinica/<int:pk>', vistaClinica.as_view(), name='vistaClinicas'),
    path('crear-clinica/', clinicaCrear.as_view(), name='nuevaClinica'),
    path('eliminar-clinica/<int:pk>', eliminarClinica.as_view(), name='eliminarClinica'),
    path('editar-clinica/<int:pk>', editarClinica.as_view(), name='editarClinica'),
]

