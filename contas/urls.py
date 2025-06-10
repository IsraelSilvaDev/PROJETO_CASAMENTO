"""
Este arquivo de URLs do Django (contas/urls.py) define as rotas relacionadas à autenticação dos usuários. Ele faz o seguinte:

Inclui todas as URLs padrão do Django para autenticação, como login, logout e senha, usando include('django.contrib.auth.urls'). Essas rotas são acessíveis na URL raiz ('').
Define uma rota personalizada 'registrar/', que aponta para a função registrar na views, permitindo que os usuários se registrem no sistema. Essa rota tem o nome 'registrar' para facilitar referências."""

# contas/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')), # Inclui login, logout, etc.
    path('registrar/', views.registrar, name='registrar'),
]