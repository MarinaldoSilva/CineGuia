from rest_framework import generics, viewsets
from .models import Filme, Diretor, Genero
from .serializers import DiretorSerializer, FilmeSerializer, GeneroSerializer

class DiretorViewSet(viewsets.ModelViewSet):
    serializer_class = DiretorSerializer
    queryset = Diretor.objects.all()

class GeneroViewSet(viewsets.ModelViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()

class FilmeListCreateView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

    """podemos filtrar por esses campos"""
    filterset_fields = ['titulo', 'genero', 'diretor', 'ano_lancamendo']

class FilmeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
