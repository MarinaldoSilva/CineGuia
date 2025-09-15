# API CineGuia

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-3.14+-A30000?style=for-the-badge&logo=django)

API desenvolvida com Django e Django REST Framework para catalogar e pesquisar uma coleção pessoal de filmes. Este projeto foi criado como um exercício prático para treinar os conhecimentos em modelagem, serialização e a implementação de filtros em APIs.

## Funções

* **CRUD** para Filmes, Gêneros e Diretores.
* **Buscas e filtros** na lista de filmes:
    * Ano de lançamento (`?ano_lancamento=2010`)
    * Gênero (`?genero=1`)
    * Diretor (`?diretor=2`)
* **Relacionamentos** que permitem criar/atualizar filmes usando o nome do Gênero e do Diretor, em vez de seus IDs, ficando mais fácil a leitura e visualização do seu catálogo (`SlugRelatedField`).
* **Arquitetura** utilizando tanto `Viewsets` (para Gêneros e Diretores) quanto `Generic Views` (para Filmes), utilizei essas diferentes padrões para treinar e solidificar esse conhecimento.

## Tecnologias

* Python
* Django
* Django REST Framework (DRF)
* django-filter
* SQLite3 (Banco de dados para desenvolvimento)
