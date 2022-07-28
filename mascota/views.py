from .models import Gato
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView


class ListadoGatos(ListView):
    model=Gato
    template_name = 'Gato/listado_gatos.html'
    
    
class CrearGato(CreateView):
    model=Gato
    template_name = 'Gato/crear_gato.html'
    success_url = '/mascotas/gatos'
    fields = ['apodo', 'edad', 'fecha_creacion']

    
class EditarGato(UpdateView):
    model=Gato
    template_name = 'Gato/editar_gato.html'
    success_url = '/mascotas/gatos'
    fields = ['apodo', 'edad', 'fecha_creacion']
    
    
class EliminarGato(DeleteView):
    model=Gato
    template_name = 'Gato/eliminar_gato.html'
    success_url = '/mascotas/gatos'
    
    
class MostrarGato(DetailView):
    model=Gato
    template_name = 'Gato/mostrar_gato.html'