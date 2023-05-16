from django.shortcuts import render,ListView
from exemplo.models import Administradores

class AdminList(ListView):
    model = Administradores
    queryset = Administradores.objects.all()