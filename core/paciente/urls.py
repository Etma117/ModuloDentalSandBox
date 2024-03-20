from django.urls import path, include
from .views import home, mostrar_formulario

urlpatterns = [

    path("home", mostrar_formulario, name='Paciente' ),    
]