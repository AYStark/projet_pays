from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=100, default="aucun")
    specialite = models.CharField(max_length=100, default="aucun")

class Eleve(models.Model):
    nom = models.CharField(max_length=100, default="aucun")
    lieu_de_naissance = models.CharField(max_length=100, default="aucun")
    date_de_naissance = models.CharField(max_length=100, default="aucun")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
