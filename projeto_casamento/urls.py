"""
Define as rotas (URLs) do site, especificando quais views (páginas) serão carregadas para cada URL solicitada.

Importações:

admin: para acessar a interface administrativa padrão do Django.
path e include: para definir e incluir URLs de aplicativos.
settings e static: para trabalhar com arquivos estáticos e de mídia durante o desenvolvimento.
urlpatterns:

path('admin/', admin.site.urls): rota para o painel administrativo do Django.
path('', include('galeria.urls')): inclui as URLs do aplicativo galeria. A raiz do site ('') aponta para as URLs definidas dentro do galeria.
path('contas/', include('contas.urls')): todas as URLs que começam com contas/ serão gerenciadas pelo aplicativo contas.
Servir arquivos de mídia em modo de desenvolvimento:

A condição if settings.DEBUG: verifica se o projeto está em modo de desenvolvimento.
Se estiver, adiciona ao urlpatterns uma rota para servir arquivos de mídia (MEDIA_URL) que estão na pasta MEDIA_ROOT. Assim, as imagens e outros arquivos enviados pelos usuários ficam acessíveis durante o desenvolvimento.
"""
# projeto_casamento/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),  # Inclui as URLs da galeria
    path('contas/', include('contas.urls')),  # Inclui as URLs de contas
]

# Rota para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)