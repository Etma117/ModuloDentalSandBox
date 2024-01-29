from django.urls import path
from . import views
from .views import clinicaCrear, Clinicas, vistaClinica, eliminarClinica

urlpatterns = [
    path('verClinicas/', Clinicas.as_view(), name='clinicas'),
    path('clinica/<int:pk>', vistaClinica.as_view(), name='vistaClinicas'),
    path('crearClinica/', clinicaCrear.as_view(), name='nuevaClinica'),
    path('eliminarClinica/<int:pk>', eliminarClinica.as_view(), name='eliminarClinica'),
]
