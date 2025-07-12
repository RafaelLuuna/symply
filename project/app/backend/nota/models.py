from django.db import models

# Create your models here.
class Nota(models.Model):
    """Model definition for Nota."""

    titulo = models.CharField(max_length=255, verbose_name='Título')
    conteudo = models.TextField(verbose_name='Conteúdo')
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('bom', 'bom'),
            ('ruim', 'ruim'),
        ],
    )
    data_acontecimento = models.DateTimeField(verbose_name='Data do Acontecimento')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_update = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    # TODO: Define fields here

    class Meta:
        """Meta definition for Nota."""

        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        """Unicode representation of Nota."""
        return self.titulo

    def get_absolute_url(self):
        """Return absolute url for Nota."""
        return ('')

    # TODO: Define custom methods here
