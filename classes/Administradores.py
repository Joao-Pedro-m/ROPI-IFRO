from django.db import models


class Administradores(models.Model):
    id = models.AutoField()
    nome = models.CharField(max_length=45)
    matricula_API = models.BigIntegerField()
    senha_API = models.CharField(max_length=45)