from django import forms
from exemplo.models import Administradores

class AdminForm(forms.ModelForm):
    class Meta:
        model = Administradores
        fields = '__all__'
        
        