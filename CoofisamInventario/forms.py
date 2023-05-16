from django import forms
from .models import Equipos

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = '__all__'