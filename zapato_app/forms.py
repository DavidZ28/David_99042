from django import forms
from .models import Ubicacion, Zapato, Pedido

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'direccion']

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        exclude = ()

class PedidoForm(forms.ModelForm):
    ESTADO_CHOICES = [
        ('pagado', 'Pagado'),
        ('pendiente', 'Pendiente'),
        ('cancelado', 'Cancelado'),
    ]

    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pedido
        fields = ['zapato', 'cantidad', 'estado']
