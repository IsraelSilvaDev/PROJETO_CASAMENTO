# galeria/models.py
from django.db import models
from django.contrib.auth.models import User

class Foto(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='fotos_galeria/')
    legenda = models.TextField(blank=True, null=True)
    data_upload = models.DateTimeField(auto_now_add=True)
    aprovada = models.BooleanField(default=False)
    curtidas = models.ManyToManyField(User, related_name='fotos_curtidas', blank=True)

    def __str__(self):
        return f'Foto de {self.autor.username} - Aprovada: {self.aprovada}'

    def total_curtidas(self):
        return self.curtidas.count()

class Comentario(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_criacao']

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.foto}'