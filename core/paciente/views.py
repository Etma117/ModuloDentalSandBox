from django.shortcuts import render
from usuarios.models import CustomUser
from clinicas.models import Clinica
from django.contrib.auth.models import Group

from .forms import CitasFormP

# Create your views here.
def home(request):
    return render(request, 'agendar_cita.html')

def mostrar_formulario(request):
    grupo_dentista = Group.objects.get(name='Dentista')

    dentistas_grupo = grupo_dentista.user_set.all()

    clinicas = Clinica.objects.all()
    form = CitasFormP()  

    context = {
        'dentistas': dentistas_grupo,
        'clinicas': clinicas,
        'form': form,
    }
    return render(request, 'agendar_cita.html', context)