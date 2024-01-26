from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CitaListar, CitaDetailView, CitaCrearView, CitaUpdateView, CitaDeleteView


urlpatterns = [
    path('', CitaListar.as_view(), name='Citas' ),
    path('CitaCrear', CitaCrearView.as_view(), name= 'CitaCrear'),
    path('DetalleCita/<int:pk>',CitaDetailView.as_view(), name= 'Detalle_Cita'),
    path('CitaModificar/<int:pk>/',CitaUpdateView.as_view(), name='Editar_Cita'),
    path('CitaCancelar/<int:pk>/', CitaDeleteView.as_view(), name='Cancelar_Cita'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
