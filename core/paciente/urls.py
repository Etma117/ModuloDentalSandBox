from django.urls import path, include
from .views import home, mostrar_formulario, filtrar_dentistas, filtrar_clinicas_por_municipio

urlpatterns = [

    path("home", mostrar_formulario, name='Paciente' ),
    
    #Filtros
    path('filtrar-clinicas/', filtrar_clinicas_por_municipio, name='filtrar_clinicas_por_municipio'),
    path('filtrar_dentistas/', filtrar_dentistas, name='filtrar_dentistas'),    
]