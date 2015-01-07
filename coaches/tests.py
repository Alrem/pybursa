from django.test import TestCase, Client

# Create your tests here.
class CoachesTests(TestCase):

    def test_page(self):
        client = Client()

        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)