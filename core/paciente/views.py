from django.shortcuts import render
from usuarios.models import CustomUser
from clinicas.models import Clinica, Municipio
from django.contrib.auth.models import Group
from django.http import JsonResponse

from .forms import CitasFormP

# Create your views here.
def home(request):
    return render(request, 'agendar_cita.html')

def mostrar_formulario(request):
    grupo_dentista = Group.objects.get(name='Dentista')
    dentistas_grupo = grupo_dentista.user_set.all()

    clinicas = Clinica.objects.all()
    municipios= Municipio.objects.all()
    form = CitasFormP()  

    context = {
        'dentistas': dentistas_grupo,
        'municipios' : municipios,
        'clinicas': clinicas,
        'form': form,
    }
    return render(request, 'agendar_cita.html', context)

def filtrar_clinicas_por_municipio(request):
    municipio_id = request.GET.get('municipio_id')
    if municipio_id:
        clinicas = Clinica.objects.filter(municipio=municipio_id)
        clinicas_data = [{'id': clinica.id, 'nombre': clinica.nombre} for clinica in clinicas]
        return JsonResponse({'clinicas': clinicas_data})
    else:
        return JsonResponse({'error': 'Municipio no especificado'}, status=400)

def filtrar_dentistas(request):
    clinica_id = request.GET.get('clinica_id')
    if clinica_id:
        clinica = Clinica.objects.get(id=clinica_id)
        grupo_dentista = Group.objects.get(name='Dentista')
        dentistas_grupo = grupo_dentista.user_set.filter(clinicas=clinica)

        dentistas_data = [{'id': dentista.id, 'nombre': dentista.get_full_name()} for dentista in dentistas_grupo]

        return JsonResponse({'dentistas': dentistas_data})
    else:
        return JsonResponse({'error': 'Clínica no especificada'}, status=400)