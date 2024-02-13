from django.urls import path

from .views import EventosView, CitaCrearView, CitaEditarView

urlpatterns = [
    path('', EventosView.as_view(), name='Agenda' ),
    path('crear-cita',CitaCrearView.as_view(), name='CrearCita'),    
    path('editar-cita/<int:pk>/',CitaEditarView.as_view(), name='EditarCita')

]

