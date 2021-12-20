from django.test import TestCase
from .forms import SignUpForm

# Create your tests here.


class TestSignUpForm(TestCase):
    def test_first_name_is_required(self):
        form = SignUpForm({
            'first_name': '',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'me'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

    def test_last_name_is_required(self):
        form = SignUpForm({
            'first_name': 'Harry',
            'last_name': '',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'me'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = SignUpForm({
            'first_name': 'Harry',
            'last_name': 'Smith',
            'email': '',
            'username': 'HarryS',
            'password': 'me'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
    
    def test_username_is_required(self):
        form = SignUpForm({
            'first_name': 'Harry',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': '',
            'password': 'me'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_password_is_required(self):
        form = SignUpForm({
            'first_name': 'Harry',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors.keys())
        self.assertEqual(form.errors['password'][0], 'This field is required.')

    def test_password_must_be_at_least_8_characters(self):
        form = SignUpForm({
            'first_name': 'Harry',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'me'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors.keys())
