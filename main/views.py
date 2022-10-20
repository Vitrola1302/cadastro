from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Animal

class HomeView(TemplateView):
    template_name = 'main/index.html'
    
class ListaAnimalView(ListView):
    model = Animal
    queryset = Animal.objects.all().order_by('nome_completo')
