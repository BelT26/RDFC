from django.test import TestCase
from .forms import MyCustomSignupForm, MatchForm, ResultsForm

# Create your tests here.
class TestCustomSignupForm(TestCase):

    def test_first_name_is_required(self):
        form = MyCustomSignupForm({
            'first_name': '',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'football'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

        def test_last_name_is_required(self):
            form = MyCustomSignupForm({
                'first_name': 'Harry',
                'last_name': '',
                'email': 'harry@gmail.com',
                'username': 'HarryS',
                'password': 'football'
            })
            self.assertFalse(form.is_valid())
            self.assertIn('last_name', form.errors.keys())
            self.assertEqual(form.errors['last_name'][0], 'This field is required.')


class TestMatchForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MatchForm()
        self.assertEqual(form.Meta.fields, ['match_date', 'time', 'location'])


class TestResultsForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ResultsForm()
        self.assertEqual(form.Meta.fields, ['match_date', 'time', 'location', 'blue_goals', 'white_goals'])