from django import forms
from .models import ConsultaComposta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = ConsultaComposta
        fields = ['nombre', 'pregunta']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej. Ana García', 'class': 'form-input'}),
            'pregunta': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ej. Mi composta huele un poco a amoníaco, ¿qué hago?', 'class': 'form-input'}),
        }

class CalculadoraForm(forms.Form):
    cantidad_verdes = forms.FloatField(
        min_value=0.1,
        label="Cantidad de residuos verdes (kg o litros)",
        widget=forms.NumberInput(attrs={'step': '0.5', 'placeholder': 'Ej. 2.5', 'class': 'form-input'})
    )