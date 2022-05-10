from django.test import TestCase
from .forms import MyCustomSignupForm, MatchForm, ResultsForm


# Create your tests here.
class TestCustomSignupForm(TestCase):
    """
    Tests that required fields must be completed in the
    CustomSignUpForm
    """
    def test_first_name_is_required(self):
        """
        Check that the first name is required
        """
        form = MyCustomSignupForm({
            'first_name': '',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'football'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')

    def test_last_name_is_required(self):
        """
        Check that the last name is required
        """
        form = MyCustomSignupForm({
            'first_name': 'Harry',
            'last_name': '',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'football'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')


class TestMatchForm(TestCase):
    """
    Tests for the MatchForm
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Checks that the correct fields are displayed
        """
        form = MatchForm()
        self.assertEqual(form.Meta.fields, ['match_date', 'time', 'location'])


class TestResultsForm(TestCase):
    """
    Tests for the ResultsForm
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Checks that the correct fields are displayed
        """
        form = ResultsForm()
        self.assertEqual(form.Meta.fields, ['match_date', 'time', 'location',
                         'blue_goals', 'white_goals'])
