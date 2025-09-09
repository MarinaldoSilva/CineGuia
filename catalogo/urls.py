from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiretorViewSet, GeneroViewSet, FilmeListCreateView, FilmeRetrieveUpdateDestroy

router = DefaultRouter()
router.register(r'generos', GeneroViewSet)
router.register(r'diretor', DiretorViewSet)

urlpatterns = [
    #url viewsets
    path('', include(router.urls)),

    #url generics
    path('filmes/', FilmeListCreateView.as_view(), name='filme_list'),
    path('filmes<int:pk>/', FilmeRetrieveUpdateDestroy.as_view(), name='filme_detail')
]
