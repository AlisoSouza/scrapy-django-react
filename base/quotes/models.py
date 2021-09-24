from django.db import models


class Author(models.Model):
    """Classe que representa um Autor"""
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.author}'


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tag}'


class Quote(models.Model):
    """Classe que representa uma Quote"""
    quote = models.TextField(verbose_name='Quote')
    author = models.ForeignKey(
        Author, verbose_name='Author', on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.author}: {self.quote}'

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
