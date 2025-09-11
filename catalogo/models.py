from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome}"
    
class Diretor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nome}"
    
class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    ano_lancamento = models.IntegerField()
    nota_imdb = models.DecimalField(max_digits=3, decimal_places=1)
    """Se alguém deletar um gênero que ainda tem filmes associados a ele, a exclusão não é permitida"""
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, related_name='filmes')

    def __str__(self):
        return f"{self.titulo}, lançado em {self.ano_lancamento} está classificado no IMDB com nota {self.nota_imdb}"
