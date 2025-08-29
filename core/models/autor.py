from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(("Email address"), max_length=100)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
