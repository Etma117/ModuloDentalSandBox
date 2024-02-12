from django.urls import path

from .views import EventosView, CitaCrearView

urlpatterns = [
    path('', EventosView.as_view(), name='Agenda' ),
    path('crear-cita',CitaCrearView.as_view(), name='CrearCita')

]

