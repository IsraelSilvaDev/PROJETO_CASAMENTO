# contas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('galeria_principal')
    else:
        form = RegistroForm()
    return render(request, 'registration/registrar.html', {'form': form})