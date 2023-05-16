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
    
    
class Cursos(models.Model):
    id = models.AutoField()
    tipo_curso = models.CharField(max_length=45)
    
class Ano(models.Model):
    id = models.AutoField()
    ano = models.IntegerField()
    
    
class Administradores(models.Model):
    id = models.AutoField()
    nome = models.CharField(max_length=45)
    matricula_API = models.BigIntegerField(blank=True,null=True)
    senha_API = models.CharField(max_length=45,blank=True,null=True)
    
    def __str__(self):
        return self.nome
    
    