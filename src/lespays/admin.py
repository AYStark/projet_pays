from django.contrib import admin
from .models import Classe, Eleve

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom','specialite')  

admin.site.register(Classe, ClasseAdmin)

class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom', 'lieu_de_naissance', 'date_de_naissance', 'classe') 
admin.site.register(Eleve, EleveAdmin)
