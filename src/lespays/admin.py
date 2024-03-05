from django.contrib import admin
from .models import Continent, Pays


class ContinentAdmin(admin.ModelAdmin):
    list_display = ('nom',)  

admin.site.register(Continent, ContinentAdmin)

class PaysAdmin(admin.ModelAdmin):
    list_display = ('nom', 'devise', 'superficie', 'continent') 
admin.site.register(Pays, PaysAdmin)