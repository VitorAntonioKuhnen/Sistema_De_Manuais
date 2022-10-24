from django.db import models

class Manuais(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()


    class Meta:
        db_table = 'Manuais'

    def __str__(self):
        return self.titulo
