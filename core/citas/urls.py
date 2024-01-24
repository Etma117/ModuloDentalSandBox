from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CitaListar, CitaDetailView, CitaCrearView


urlpatterns = [
    path('', CitaListar.as_view(), name='Citas' ),
    path('CitaCrear', CitaCrearView.as_view(), name= 'CitaCrear'),
    path('DetalleCita/<int:pk>', CitaCrearView.as_view(), name= 'Detalle_Cita')
    #path('AccesorioModificar/<int:pk>/', AccesorioEditarView.as_view(), name="AccesorioEditar"),
   # path('AccesorioEliminar/<int:pk>/', AccesorioEliminarView.as_view(), name='AccesorioEliminar'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
