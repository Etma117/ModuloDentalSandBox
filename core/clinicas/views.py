from django.shortcuts import render

def clinicas(request):
    return render(request, 'clinicas.html')

def vistaClinica(request):
    return render(request, 'vistaclinicas.html')