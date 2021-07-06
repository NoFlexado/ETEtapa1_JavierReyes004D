from django.shortcuts import render,redirect
from .models import Colaboradores
from .forms import AgrColab,modColab


# Create your views here.

def Inicio(request):
    return render(request,'Inicio.html')

def Lista(request):
    Colabora = Colaboradores.objects.all()
    return render(request,'Lista.html',context={'InfoAdm': Colabora})

def Crear(request):
    if request.method == 'POST':
        CrearColab = AgrColab(request.POST, files=request.FILES)
        if CrearColab.is_valid():
            CrearColab.save()
            return redirect('Inicio')
    else:
        CrearColab = AgrColab()
    return render(request,'core/Crear.html', {'CrearColab': CrearColab})

def ModificarColab(request, id ):
    modiColab = Colaboradores.objects.get(rutColaborador=id)
    if request.method == 'POST':
        modiColab = modColab(data=request.POST, files=request.FILES, instance=modiColab)
        if modiColab.is_valid():
            modiColab.save()
            return redirect('Lista')
    else:
        modiColab = modColab(instance=modiColab)
    return render(request,'core/Modificar.html', {'modiColab': modiColab})

def EliminarColab(request, id):
    EliColab = Colaboradores.objects.get(rutColaborador=id)
    EliColab.delete()
    return redirect('Lista')


