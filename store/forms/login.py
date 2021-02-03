from django import forms
from django.forms.widgets import PasswordInput, TextInput


class Login_form(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        min_length=6,
        widget=PasswordInput(attrs={'class': 'form-control form-control-sm'})
    )
