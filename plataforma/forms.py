from django import forms
from .models import Productor, Producto

class ProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = ['nombre', 'contrasena', 'telefono', 'correo', 'vereda', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario único (Ej: juan_finca)'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña de acceso'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3101234567 (WhatsApp)'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com (Opcional)'}),
            'vereda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Guaimaral, El Desastre...'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '¿Qué produces o elaboras?'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['productor', 'categoria', 'nombre', 'descripcion', 'precio', 'imagen']
        widgets = {
            'productor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Bolis de Corozo...'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe el producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio en COP'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }