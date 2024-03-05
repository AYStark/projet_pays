from django.urls import path
from lespays import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('ajouter_continent/', views.ajouter_continent, name='ajouter_continent'),
    path('ajouter_pays/<int:continent_id>/', views.ajouter_pays, name='ajouter_pays'),
    path('detail_continent/<int:continent_id>/', views.detail_continent, name='detail_continent'),
    path('supprimer_continent/<int:continent_id>/', views.supprimer_continent, name='supprimer_continent'),
    path('supprimer_pays/<int:pays_id>/', views.supprimer_pays, name='supprimer_pays'),
]