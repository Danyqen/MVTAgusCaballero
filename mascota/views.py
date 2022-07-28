from .models import Gato
from django.views.generic.list import ListView
from django.views.generic.list import DeleteView, UpdateView, CreateView
# from django.views.generic.list import View


class ListadoGatos(ListView):
    model=Gato
    template_name = 'Gato/listado_gatos.html'
    
    
class CrearGato(CreateView):
    model=Gato
    template_name = 'Gato/crear_gatos.html'
    success_url = 'gatos'
    
    
class EditarGato(UpdateView):
    model=Gato
    template_name = 'Gato/editar_gatos.html'
    success_url = 'gatos'
    success_url = 'gatos'
    
    
class EliminarGato(DeleteView):
    model=Gato
    template_name = 'Gato/eliminar_gatos.html'
    success_url = 'gatos'
    
    
# class MostrarGato(View):
#     ...