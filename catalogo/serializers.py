from rest_framework import serializers
from .models import Filme, Diretor, Genero

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['titulo','ano_lancamento', 'nota_imdb', 'genero', 'diretor']

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = ['nome']

class GeneroSerializer(serializers.ModelSerializer):
    """Ao invés de mostrar somente o ID que é o formato padrão quando se trabalha
    vamos mostrar o o retorno padrão do __str__(self)""" 
    #genero = serializers.StringRelatedField()
    #diretor = serializers.StringRelatedField()

    class Meta:
        model = Genero
        fields = ['nome']  
