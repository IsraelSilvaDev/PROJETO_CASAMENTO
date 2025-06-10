"""
Este arquivo urls.py define as rotas (URLs) do aplicativo "galeria". Cada rota mapeia uma URL específica para uma função de visualização (view) que processa a requisição.

path('', views.galeria_principal, name='galeria_principal'):
A rota raiz da galeria, que exibe a página principal da galeria de fotos.

path('foto/<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'):
Mostra os detalhes de uma foto específica, identificada pelo foto_id. O <int:foto_id> captura um número inteiro da URL.

path('upload/', views.upload_foto, name='upload_foto'):
Guia para uma página onde o usuário pode enviar (fazer upload) de uma nova foto.

path('curtir/<int:foto_id>/', views.curtir_foto, name='curtir_foto'):
Permite ao usuário "curtir" uma foto específica, identificada pelo foto_id.

path('aprovar/', views.lista_aprovacao, name='lista_aprovacao'):
Exibe uma lista de fotos pendentes para aprovação.

path('aprovar/<int:foto_id>/', views.aprovar_foto, name='aprovar_foto'):
Permite aprovar uma foto específica, identificada pelo foto_id."""


# galeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria_principal, name='galeria_principal'),
    path('foto/<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'),
    path('upload/', views.upload_foto, name='upload_foto'),
    path('curtir/<int:foto_id>/', views.curtir_foto, name='curtir_foto'),
    path('aprovar/', views.lista_aprovacao, name='lista_aprovacao'),
    path('aprovar/<int:foto_id>/', views.aprovar_foto, name='aprovar_foto'),
]