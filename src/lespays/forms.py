from django import forms
from .models import Classe, Eleve

class FormClasse(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom','specialite']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control form-control-lg'}) 
        }

class FormEleve(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'lieu_de_naissance', 'date_de_naissance']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),  # Ajouter la classe 'form-control-lg' de Bootstrap
            'lieu_de_naissance': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),  # Ajouter la classe 'form-control-lg' de Bootstrap
            'date_de_naissance': forms.NumberInput(attrs={'class': 'form-control'})  # Conserver la classe 'form-control' de Bootstrap
        }
