from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    corpo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.titulo

    def snippet(self):
        return self.corpo[:50] + '...'
