from django import forms
from django.contrib.auth.models import User
from rango.models import Bar, Tapas, UserProfile

class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128,help_text="Nombre del bar: ")
    direccion = forms.CharField(max_length=200, help_text="Direccion del bar: ")
    numero_visitas = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Bar
        fields=('nombre','direccion')

class TapaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Nombre de la tapa")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Tapas
        fields = ('nombre','picture')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
