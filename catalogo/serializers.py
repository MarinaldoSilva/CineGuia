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
    class Meta:
        model = Genero
        fields = '__all__'  


"""
Ao invés de mostrar somente o ID que é o formato padrão quando se trabalha
vamos mostrar o o retorno padrão do __str__(self)
    genero = serializers.StringRelatedField()
    diretor = serializers.StringRelatedField()

ao inves d epassar o id, podemos passar oi nome diretamente na hora do cadastro, com isso tambpem queremos garantir que o genero seja unico, e botamos um 'unique = True' no nosso model genero e diretor

    genero = serializers.SlugRelatedField(
        slug_field='nome',  # Qual campo do modelo Genero deve ser usado como identificador
        queryset=Genero.objects.all()  # Onde o DRF deve procurar por esse nome
    )
"""