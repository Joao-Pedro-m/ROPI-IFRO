from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from exemplo.models import ProjetosIntegradores

class ProjetosIntegradoresList(ListView):
    model = ProjetosIntegradores
    queryset = ProjetosIntegradores.objects.all()

class ProjetosIntegradoresCreate(CreateView):
    model = ProjetosIntegradores
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')


class ProjetosIntegradoresUpdate(UpdateView):
    model = ProjetosIntegradores
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

