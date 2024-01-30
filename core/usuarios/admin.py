from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Administrador, Medico
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.html import mark_safe

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    # Este es el método que añadimos
    def foto_preview(self, obj):
        if obj.foto:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.foto.url,
                width=50,
                height=50,
            ))
        return "Sin imagen"
    foto_preview.short_description = 'Foto'
    
    list_display = ['username', 'email', 'tipo_usuario', 'fecha_nacimiento', 'numero', 'is_active', 'is_staff', 'foto_preview']

    # Para el cambio de usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'foto', 'tipo_usuario', 'fecha_nacimiento', 'numero')}),
        ('Clínicas asociadas', {'fields': ('clinicas',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
        ('Preguntas de Seguridad', {'fields': ('pregunta_seguridad_1', 'respuesta_seguridad_1','pregunta_seguridad_2', 'respuesta_seguridad_2')}),

    )
    
    # Para crear un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'foto', 'tipo_usuario', 'fecha_nacimiento', 'numero', 'clinicas')}
        ),
    )


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['user', 'dato_especifico_admin']

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['user', 'cedula_profesional']
    
admin.site.register(CustomUser, CustomUserAdmin)

