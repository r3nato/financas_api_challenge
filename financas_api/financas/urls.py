from django.urls import path, include
from . import views, serializers
from rest_framework import routers

router = routers.DefaultRouter()
router.register('despesas', views.DespesaViewset, 'despesas')
router.register('receitas', views.ReceitaViewset, 'receitas')

urlpatterns = [
    path('', include(router.urls), name='listar'),
    path(
        'despesas/<int:ano>/<int:mes>/', 
        views.TransacoesMes.as_view(
            tipo='despesa',
            serializer_class=serializers.ReceitaSerializer
        ),
        name="despesas-mes"
    ),
    path(
        'receitas/<int:ano>/<int:mes>/', 
        views.TransacoesMes.as_view(
            tipo='receita',
            serializer_class=serializers.ReceitaSerializer
        ),
        name="receitas-mes"
    ),
]