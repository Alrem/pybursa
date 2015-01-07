from django.test import TestCase, Client
from students.models import Student

# Create your tests here.

class StudentsTests(TestCase):

    def test_page(self):
        client = Client()

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
