from django import forms

from .models import User, Show

class Register(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=20)
    password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

class Reserve(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=20)
    password = forms.CharField(label='Hasło', max_length=100, widget=forms.PasswordInput)

class NewShow(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['id', 'name', 'description', 'date', 'hour']