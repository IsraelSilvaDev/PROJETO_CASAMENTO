# galeria/forms.py
from django import forms
from .models import Foto, Comentario

class FotoUploadForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagem', 'legenda']
        widgets = {
            'legenda': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Adicione uma legenda divertida!'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Adicione um comentário...'}),
        }
        labels = {
            'texto': ''
        }