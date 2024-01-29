from django.urls import path
from .views import PacienteListView

urlpatterns = [
    # ... tus otras URLs
    path('ver-pacientes/', PacienteListView.as_view(), name='ver_pacientes'),
]
