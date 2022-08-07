from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('despesas', views.DespesaViewset, 'despesas')
router.register('receitas', views.ReceitaViewset, 'receitas')

urlpatterns = [
    path('', include(router.urls), name="listar"),
]