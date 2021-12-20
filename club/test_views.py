from django.test import TestCase
from .models import Member

# Create your tests here.


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')

    def test_get_social_page(self):
        response = self.client.get('/social')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/social.html')

    def test_get_sign_up_page(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/signup.html')

    def test_get_members_page(self):
        response = self.client.get('/members')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/members.html')

    def test_create_new_member(self):
        response = self.client.post('/signup', {
            'first_name': 'Harry',
            'last_name': 'Smith',
            'email': 'harry@gmail.com',
            'username': 'HarryS',
            'password': 'football'
        })
        self.assertRedirects(response, '/thankyou')
