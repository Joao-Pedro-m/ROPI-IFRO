from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from exemplo.models import ProjetosIntegradores,Imagem


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

class ProjetosIntegradoresDetail(DetailView):
    model = ProjetosIntegradores


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Imagem.objects.create(Imagem=image)
