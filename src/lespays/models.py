from django.db import models

class Continent(models.Model):
    nom = models.CharField(max_length=100)

class Pays(models.Model):
    nom = models.CharField(max_length=100)
    devise = models.CharField(max_length=100)
    superficie = models.FloatField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)