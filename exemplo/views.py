from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from exemplo.models import ProjetosIntegradores
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from exemplo.models import ProjetosIntegradores

class ProjetosIntegradoresList(ListView):
    model = ProjetosIntegradores
    queryset = ProjetosIntegradores.objects.all()
class ProjetosIntegradoresList(ListView):
    model = ProjetosIntegradores
    queryset = ProjetosIntegradores.objects.all()

class ProjetosIntegradoresCreate(CreateView):
    model = ProjetosIntegradores
class ProjetosIntegradoresCreate(CreateView):
    model = ProjetosIntegradores
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')


class ProjetosIntegradoresUpdate(UpdateView):
    model = ProjetosIntegradores
class ProjetosIntegradoresUpdate(UpdateView):
    model = ProjetosIntegradores
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

class ProjetosIntegradoresDetail(DetailView):
    model = ProjetosIntegradores