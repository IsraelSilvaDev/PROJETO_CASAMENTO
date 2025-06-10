# galeria/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Foto
from .forms import FotoUploadForm, ComentarioForm

def galeria_principal(request):
    fotos = Foto.objects.filter(aprovada=True).order_by('-data_upload')
    return render(request, 'galeria/galeria_principal.html', {'fotos': fotos})

def detalhe_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id, aprovada=True)
    comentarios = foto.comentarios.all()
    
    # Lógica de Comentários
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.foto = foto
            novo_comentario.autor = request.user
            novo_comentario.save()
            return redirect('detalhe_foto', foto_id=foto.id)
    else:
        comentario_form = ComentarioForm()

    # Lógica de Curtidas
    curtido = False
    if request.user.is_authenticated and foto.curtidas.filter(id=request.user.id).exists():
        curtido = True

    return render(request, 'galeria/detalhe_foto.html', {
        'foto': foto, 
        'comentarios': comentarios,
        'comentario_form': comentario_form,
        'curtido': curtido
    })


@login_required
def upload_foto(request):
    if request.method == 'POST':
        form = FotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.autor = request.user
            foto.save()
            return render(request, 'galeria/upload_sucesso.html')
    else:
        form = FotoUploadForm()
    return render(request, 'galeria/upload_foto.html', {'form': form})

@login_required
def curtir_foto(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)
    if foto.curtidas.filter(id=request.user.id).exists():
        foto.curtidas.remove(request.user)
    else:
        foto.curtidas.add(request.user)
    return redirect('detalhe_foto', foto_id=foto.id)

# Função para verificar se o usuário é admin/staff
def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def lista_aprovacao(request):
    fotos_pendentes = Foto.objects.filter(aprovada=False).order_by('data_upload')
    return render(request, 'galeria/lista_aprovacao.html', {'fotos': fotos_pendentes})

@user_passes_test(is_staff_user)
def aprovar_foto(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)
    foto.aprovada = True
    foto.save()
    return redirect('lista_aprovacao')