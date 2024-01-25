from django.shortcuts import render

def clinicas(request):
    return render(request, 'clinicas.html')

def vistaClinica(request):
    return render(request, 'vistaclinicas.html')

def crearClinica(request):
    return render(request, 'nuevaClinica.html')

def clinicaFormulario(request):
    form = clinicaForm(request.POST)
    if form.is_valid():
        return redirect("clinicas")
    else:
        return render (request, "nuevaClinica.html", {"form": form })