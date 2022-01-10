from django import forms
from .models import ClubMember
from allauth.account.forms import SignupForm 


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
 
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


# class SignUpForm(forms.Form):
#     first_name = forms.CharField(max_length=50, min_length=2)
#     last_name = forms.CharField(max_length=50, min_length=2)
#     username = forms.CharField(max_length=50, min_length=2)
#     email = forms.EmailField(max_length=200)
#     password = forms.CharField(max_length=50, min_length=8, 
#                                widget=forms.PasswordInput)



# class LogInForm(forms.ModelForm):
#     username = forms.CharField(max_length=50, min_length=2)
#     password = forms.CharField(max_length=50, min_length=8, 
#                                widget=forms.PasswordInput)
