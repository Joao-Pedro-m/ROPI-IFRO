from django import forms
from exemplo.models import ProjetosIntegradores

class ProjetosIntegradoresForm(forms.ModelForm):
    class Meta:
        model = ProjetosIntegradores
        fields = '__all__'
