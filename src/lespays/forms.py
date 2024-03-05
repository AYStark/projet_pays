from django import forms
from .models import Continent, Pays

class FormContinent(forms.ModelForm):
    class Meta:
        model = Continent
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'})  # Ajouter la classe 'form-control-lg' de Bootstrap
        }

class FormPays(forms.ModelForm):
    class Meta:
        model = Pays
        fields = ['nom', 'devise', 'superficie']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),  # Ajouter la classe 'form-control-lg' de Bootstrap
            'devise': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),  # Ajouter la classe 'form-control-lg' de Bootstrap
            'superficie': forms.NumberInput(attrs={'class': 'form-control'})  # Conserver la classe 'form-control' de Bootstrap
        }
