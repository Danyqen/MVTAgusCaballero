import monsters
from .models import Monster
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListMonster(ListView):
    model=Monster
    template_name = 'Monster/list_monster.html'


class CreateMonster(CreateView):
    model=Monster
    template_name = 'Monster/create_monster.html'
    success_url = '/monsters/monsters'
    fields = ['nickname', 'age', 'date']
    
    
class EditMonster(UpdateView):
    model=Monster
    template_name = 'Monster/edit_monster.html'
    success_url = '/monsters/monsters'
    fields = ['nickname', 'age', 'date']

class DeleteMonster(DeleteView):
    model=Monster
    template_name = 'Monster/delete_monster.html'
    success_url = '/monsters/monsters'
    

class ShowMonster(DetailView): 
    model=Monster
    template_name = 'Monster/show_monster.html'

