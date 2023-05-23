from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from exemplo.models import Administradores

class AdministradoresList(ListView):
    model = Administradores
    queryset = Administradores.objects.all()

class AdministradoresCreate(CreateView):
    model = Administradores
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')


class AdministradoresUpdate(UpdateView):
    model = Administradores
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

