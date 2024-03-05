from django.shortcuts import render, redirect
from .models import Continent, Pays
from .forms import FormContinent, FormPays

from .serializer import ContinentSerializer, PaysSerializer
from rest_framework import viewsets


def accueil(request):
    continents = Continent.objects.all()
    return render(request, 'accueil.html', {'continents': continents})

def ajouter_continent(request):
    if request.method == 'POST':
        form = FormContinent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = FormContinent()
    return render(request, 'ajouter_continent.html', {'form': form})

def ajouter_pays(request, continent_id):
    continent = Continent.objects.get(pk=continent_id)
    if request.method == 'POST':
        form = FormPays(request.POST)
        if form.is_valid():
            pays = form.save(commit=False)
            pays.continent = continent
            pays.save()
            # Redirection vers la page de détail du continent
            return redirect('detail_continent', continent_id=continent_id)
    else:
        form = FormPays()
    return render(request, 'ajouter_pays.html', {'form': form, 'continent': continent})
    
def detail_continent(request, continent_id):
    continent = Continent.objects.get(pk=continent_id)
    pays = Pays.objects.filter(continent=continent)
    return render(request, 'detail_continent.html', {'continent': continent, 'pays': pays})

    
def supprimer_continent(request, continent_id):
    continent = Continent.objects.get(pk=continent_id)
    continent.delete()
    return redirect('accueil')

def supprimer_pays(request, pays_id):
    pays = Pays.objects.get(pk=pays_id)
    continent_id = pays.continent.id
    pays.delete()
    return redirect('detail_continent', continent_id=continent_id)

    
class Continentviewset(viewsets.ModelViewSet):
   
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

class Paysviewset(viewsets.ModelViewSet):
    
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer