from django import forms
from django.forms import Form
from django.forms.widgets import PasswordInput, TextInput


class Signup_form(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=20,
        min_length=5,
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    email = forms.EmailField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    phone = forms.CharField(
        required=True,
        max_length=13,
        min_length=10,
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        min_length=6,
        widget=PasswordInput(attrs={'class': 'form-control form-control-sm'})
    )
