from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gerar_contrato/', views.gerar_contrato, name='gerar_contrato'),
    path('consultar_cep/', views.consultar_cep, name='consultar_cep'),
]
