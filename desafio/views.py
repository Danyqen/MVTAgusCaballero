from .forms import BusquedaPerro, FormPerro

from .forms import BusquedaPerro, FormPerro
from .models import Perro
from datetime import datetime

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import BusquedaPerro, FormPerro
from .models import Perro
from datetime import datetime

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------->

def una_vista(request):
    return render(request, 'index.html')

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------->

def crear_perro(request):
    
    if request.method == 'POST':
        form = FormPerro(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now() 
            
            perro = Perro(
                nombre=data.get('nombre'), 
                edad=data.get('edad'), 
                fecha_creacion=fecha
                # fecha_creacion=fecha if fecha else datetime.now()
            )
            perro.save()
            
            # listado_perros = Perro.objects.all()
            # form = BusquedaPerro()
            # return render(request, 'listado_perros.html', {'listado_perros': listado_perros})
            return redirect('listado_perros')
        
        else:
            return render(request, 'Perro/crear_perro.html', {'form': form})
            
            
            
    
    form_perro = FormPerro()

    return render(request, 'Perro/crear_perro.html', {'form': form_perro})

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------->

def listado_perros(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado_perros = Perro.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:
        listado_perros = Perro.objects.all()
    
    form = BusquedaPerro()

    return render(request, 'Perro/listado_perros.html', {'listado_perros': listado_perros, 'form': form})

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------->

def editar_perro(request, id):
    perro = Perro.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormPerro(request.POST)
        if form.is_valid():
            perro.nombre = form.cleaned_data.get('nombre')
            perro.edad = form.cleaned_data.get('edad')
            perro.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            perro.save()
            
            return redirect('listado_perros')
        else:
            return render(request, 'Perro/editar_perro.html',{'form': form, 'perro': perro})
    
    form_perro = FormPerro(initial={'nombre': perro.nombre, 'edad': perro.edad, 'fecha_creacion': perro.fecha_creacion})
   
    return render(request, 'Perro/editar_perro.html', {'form': form_perro, 'perro': perro})
    
# <---------------------------------------------------------------------------------------------------------------------------------------------------------------->
    
def eliminar_perro(request, id):
    perro = Perro.objects.get(id=id)
    perro.delete()
    
    return redirect('listado_perros')

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------->

def mostrar_perro(request, id):
    perro = Perro.objects.get(id=id)
    return render(request, 'Perro/mostrar_perro.html', {'perro': perro})
    