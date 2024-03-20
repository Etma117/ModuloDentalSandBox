from django.urls import path, include
from .views import home, mostrar_formulario, filtrar_dentistas

urlpatterns = [

    path("home", mostrar_formulario, name='Paciente' ),
    
    #Filtros
    path('filtrar_dentistas/', filtrar_dentistas, name='filtrar_dentistas'),    
]