from django.db import models

class Cursos(models.Model):
    tipo_curso = models.CharField(max_length=45)
    def __str__(self):
        return self.tipo_curso



class ProjetosIntegradores(models.Model):
    titulo = models.CharField(max_length=45)
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()
    resumo = models.CharField(max_length=250)
    resultados = models.CharField(max_length=150)
    Curso_idCurso = models.ForeignKey(Cursos,default='', on_delete=models.CASCADE)


class Imagem(models.Model):
    Imagem = models.FileField()


class Administradores(models.Model):
    nome = models.CharField(max_length=45)
    matricula_API = models.BigIntegerField(blank=True,null=True)
    senha_API = models.CharField(max_length=45,blank=True,null=True)
    
    def _str_(self):
        return self.nome