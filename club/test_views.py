from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """
    Tests that the correct templates are returned
    """
    def test_get_home_page(self):
        """
        Tests that the home page is returned
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')

    def test_get_next_fixture(self):
        """
        Tests that the next fixture page is returned
        """
        response = self.client.get('/next_fixture')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/next_fixture.html')

    def test_get_league_table(self):
        """
        Tests that the league table page is returned
        """
        response = self.client.get('/league_table')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/league_table.html')
