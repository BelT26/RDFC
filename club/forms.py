from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    username = forms.CharField(max_length=50, min_length=2)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=50, min_length=8, widget=forms.PasswordInput)


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=2)
    password = forms.CharField(max_length=50, min_length=8, widget=forms.PasswordInput)

