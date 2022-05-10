from django import forms
from allauth.account.forms import SignupForm
from .models import Match


class MyCustomSignupForm(SignupForm):
    """
    A form for new users to sign up
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        """
        Determines the user details that are saved
        """
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class DateInput(forms.DateInput):
    """
    Used to make the the date field in the MatchForm
    """
    input_type = 'date'


class MatchForm(forms.ModelForm):
    """
    A form to add or edit a match
    """
    class Meta:
        """
        Determines the model used for the MatchForm the
        fields displayed and the widgets used
        """
        model = Match
        fields = ['match_date', 'time', 'location']
        widgets = {'match_date': DateInput()}


class ResultsForm(forms.ModelForm):
    """
    A form to add the results of a match
    """
    class Meta:
        """
        Determines the model used for the ResultsForm and the
        fields displayed
        """
        model = Match
        fields = ['match_date', 'time', 'location', 'blue_goals',
                  'white_goals']
