from django.urls import path
from .views import PacienteListView, PacienteDetailView

urlpatterns = [
    # ... tus otras URLs
    path('ver-pacientes/', PacienteListView.as_view(), name='ver_pacientes'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),

]
