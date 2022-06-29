from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registroanimales.models import Avatar

class FamiliaFormulario(forms.Form):
    id_familia= forms.IntegerField()
    apellido= forms.CharField(max_length=50)
    nombre_responsable= forms.CharField(max_length=30)
    telefono= forms.CharField(max_length=20)
    mail= forms.EmailField()

class MascotaFormulario(forms.Form):
    id_mascota= forms.IntegerField()
    nombre= forms.CharField(max_length=50)
    fecha_nacimiento= forms.DateField()
    peso_kg= forms.DecimalField(max_digits=4,decimal_places=2)
    altura_mts= forms.DecimalField(max_digits=3,decimal_places=2)

    
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['username','email','password1','password2']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail",required=False)
    password1=forms.CharField(label="Modificar Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)
    
    first_name=forms.CharField(label="Modificar nombre",widget=forms.PasswordInput,required=False)
    last_name= forms.CharField(label="Modificar apellido",widget=forms.PasswordInput,required=False)
    descripcion= forms.CharField(label="Descripción",widget=forms.PasswordInput,required=False)

    class Meta:
        model= User
        fields=['username','first_name','last_name','descripcion','email','password1','password2']
        help_texts={k:"" for k in fields}

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model= Avatar
        fields=['imagen']


