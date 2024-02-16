from django.urls import path
from . import views
from .views import clinicaCrear, Clinicas, vistaClinica, eliminarClinica, editarClinica

urlpatterns = [
<<<<<<< HEAD
    path('verClinicas/', Clinicas.as_view(), name='clinicas'),
    path('clinica/<int:clinica_id>', vistaClinica.as_view(), name='vistaClinicas'),
=======
    path('ver-clinicas/', Clinicas.as_view(), name='clinicas'),
    path('clinica/<int:pk>', vistaClinica.as_view(), name='vistaClinicas'),
>>>>>>> origin/master
    path('crearClinica/', clinicaCrear.as_view(), name='nuevaClinica'),
    path('eliminarClinica/<int:pk>', eliminarClinica.as_view(), name='eliminarClinica'),
    path('editarClinica/<int:clinica_id>', editarClinica.as_view(), name='editarClinica'),
]

