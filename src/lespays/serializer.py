from rest_framework import serializers
from lespays.models import Classe,Eleve

class ClasseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class EleveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleve
        fields = '__all__'
