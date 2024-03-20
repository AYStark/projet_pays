from django.urls import path
from lespays import views
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('ajouter_classe/', views.ajouter_classe, name='ajouter_classe'),
    path('ajouter_eleve/<int:classe_id>/', views.ajouter_eleve, name='ajouter_eleve'),
    path('detail_classe/<int:classe_id>/', views.detail_classe, name='detail_classe'),
    path('supprimer_classe/<int:classe_id>/', views.supprimer_classe, name='supprimer_classe'),
    path('supprimer_eleve/<int:eleve_id>/', views.supprimer_eleve, name='supprimer_eleve'),
]
