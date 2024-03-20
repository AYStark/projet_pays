from django.shortcuts import render, redirect
from .models import Classe, Eleve
from .forms import FormClasse, FormEleve

from .serializer import ClasseSerializer, EleveSerializer
from rest_framework import viewsets

def accueil(request):
    classes = Classe.objects.all()
    return render(request, 'accueil.html', {'classes': classes})

def ajouter_classe(request):
    if request.method == 'POST':
        form = FormClasse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = FormClasse()
    return render(request, 'ajouter_classe.html', {'form': form})

def ajouter_eleve(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    if request.method == 'POST':
        form = FormEleve(request.POST)
        if form.is_valid():
            eleve = form.save(commit=False)
            eleve.classe = classe
            eleve.save()
            # Redirection vers la page de détail du classe
            return redirect('detail_classe', classe_id=classe_id)
    else:
        form = FormEleve()
    return render(request, 'ajouter_eleve.html', {'form': form, 'classe': classe})
    
def detail_classe(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    eleve = Eleve.objects.filter(classe=classe)
    return render(request, 'detail_classe.html', {'classe': classe, 'eleve': eleve})

    
def supprimer_classe(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    classe.delete()
    return redirect('accueil')

def supprimer_eleve(request, eleve_id):
    eleve = Eleve.objects.get(pk=eleve_id)
    classe_id = eleve.classe.id
    eleve.delete()
    return redirect('detail_classe', classe_id=classe_id)

    
class Classeviewset(viewsets.ModelViewSet):
   
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class Eleveviewset(viewsets.ModelViewSet):
    
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
