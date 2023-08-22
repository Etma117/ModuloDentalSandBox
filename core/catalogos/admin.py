from django.contrib import admin
from .models import Tipos, Municipio,Responsable, Estacion, Estatus
# Register your models here.
admin.site.register(Tipos)
admin.site.register(Municipio)
admin.site.register(Responsable)
admin.site.register(Estacion)
admin.site.register(Estatus)
