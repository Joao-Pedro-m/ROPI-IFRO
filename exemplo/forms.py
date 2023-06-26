from django import form
from exemplo.models import Administradores,Imagem

class AdministradoresForm(forms.ModelForm):
    class Meta:
        model = Administradores
        fields = '__all__'

