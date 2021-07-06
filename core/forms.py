from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaboradores

class AgrColab(forms.ModelForm):
    
    class Meta:
        model = Colaboradores
        fields = ['rutColaborador','image','nombre','telefono','direccion','correo','pais','contraseña']
        labels ={
            'rutColaborador': 'Rut del Colaborador',
            'image': 'Imagen',
            'nombre': 'Nombre del Colaborador',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'correo': 'Correo',
            'pais': 'País',
            'contraseña': 'Contraseña'
        }
        widgets={
            'rutColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rutColaborador'
                }
            ), 
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Subir Imagen', 
                    'accept' : 'image/*',
                    'id': 'image'
                    
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre Completo', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Teléfono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Dirección', 
                    'id': 'direccion'
                }
            ), 
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo', 
                    'id': 'correo'
                }
            ), 
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese País', 
                    'id': 'pais'
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Contraseña', 
                    'id': 'contraseña'
                }
            ), 
        }

class modColab(forms.ModelForm):
    
    class Meta:
        model = Colaboradores
        fields = ['rutColaborador','image','nombre','telefono','direccion','correo','pais','contraseña']
        labels ={
            'rutColaborador': 'Rut del Colaborador',
            'image': 'Imagen',
            'nombre': 'Nombre del Colaborador',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'correo': 'Correo',
            'pais': 'País',
            'contraseña': 'Contraseña'
        }
        widgets={
            'rutColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rutColaborador',
                    'readonly': ''

                }
            ), 
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Subir Imagen', 
                    'accept' : 'image/*',
                    'id': 'image'
                    
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre Completo', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Teléfono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Dirección', 
                    'id': 'direccion'
                }
            ), 
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo', 
                    'id': 'correo'
                }
            ), 
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese País', 
                    'id': 'pais'
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Contraseña', 
                    'id': 'contraseña'
                }
            ), 
        }