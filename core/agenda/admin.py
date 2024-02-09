from django.contrib import admin
from schedule.models import Calendar, Event
from .models import DiasNoLaborablesCalendar, DentistaCalendar, CitasDentalesCalendar,Cita

admin.site.register(DiasNoLaborablesCalendar)
admin.site.register(DentistaCalendar)
admin.site.register(CitasDentalesCalendar)
admin.site.register(Cita)
