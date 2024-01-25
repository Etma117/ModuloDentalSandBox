from django.urls import path
from . import views

urlpatterns = [
    path('verClinicas/', views.clinicas, name='clinicas'),
    path('clinica0/', views.vistaClinica, name='vistaClinicas'),
    path('crearClinica/', views.crearClinica, name='nuevaClinica'),
]
