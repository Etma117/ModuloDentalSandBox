from django.contrib import admin
from schedule.models import Calendar, Event
from .models import DiasNoLaborablesCalendar, DentistaCalendar, CitasDentalesCalendar,Cita

class EventInline(admin.TabularInline):
    model = Event
    extra = 0  # Evita que se agreguen eventos en blanco por defecto

@admin.register(DiasNoLaborablesCalendar)
class DiasNoLaborablesCalendarAdmin(admin.ModelAdmin):
    inlines = [EventInline]

@admin.register(DentistaCalendar)
class DentistaCalendarAdmin(admin.ModelAdmin):
    inlines = [EventInline]

@admin.register(CitasDentalesCalendar)
class CitasDentalesCalendarAdmin(admin.ModelAdmin):
    inlines = [EventInline]

# admin.site.register(DiasNoLaborablesCalendar)
# admin.site.register(DentistaCalendar)
# admin.site.register(CitasDentalesCalendar)
admin.site.register(Cita)
