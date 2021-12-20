from django import forms

from .models import Member


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    username = forms.CharField(max_length=50, min_length=2)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=50, min_length=8)



