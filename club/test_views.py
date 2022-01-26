from django.test import TestCase
from .models import Member

# Create your tests here.


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')

    def test_get_next_fixture(self):
        response = self.client.get('/next_fixture')
        self.asserEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/next_fixture.html')

    def test_get_league_table(self):
        response = self.client.get('/league_table')
        self.asserEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/league_table.html')