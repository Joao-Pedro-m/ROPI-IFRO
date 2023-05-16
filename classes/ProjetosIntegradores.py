from django.db import models


class ProjetosIntegradores(models.Model):
    id = models.AutoField()
    titulo = models.CharField(max_length=45)
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()
    resumo = models.CharField(max_length=250)
    resultados = models.CharField(max_length=150)
    imagem = models.BinaryField()
    Curso_idCurso = models.IntegerField()
    Ano_idAno = models.IntegerField()
    