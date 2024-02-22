from django.urls import path
from . import views
from .views import ClinicaCrear, Clinicas, vistaClinica, eliminarClinica, editarClinica

urlpatterns = [
    path('verClinicas/', Clinicas.as_view(), name='clinicas'),
    path('clinica/<int:pk>', vistaClinica.as_view(), name='vistaClinicas'),
    path('crearClinica/', ClinicaCrear.as_view(), name='nuevaClinica'),
    path('eliminarClinica/<int:pk>', eliminarClinica.as_view(), name='eliminarClinica'),
    path('editarClinica/<int:pk>', editarClinica.as_view(), name='editarClinica'),
]
