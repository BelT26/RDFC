from django import forms
from allauth.account.forms import SignupForm
from .models import Match


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
 
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class DateInput(forms.DateInput):
    input_type = 'date'


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

