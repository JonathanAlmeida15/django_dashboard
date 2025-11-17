from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'notes']
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'notes']
        labels = {
            'notes': 'Observações',
        }
        widgets = {
            'notes': forms.Textarea(attrs={
                'rows': 3,        # Altura inicial pequena
                'class': 'form-control', 
                'style': 'resize: vertical;'  # Usuário pode expandir verticalmente
            })
        }