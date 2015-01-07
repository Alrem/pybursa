from django.test import TestCase, Client

# Create your tests here.
class CoursesTests(TestCase):

    def test_page(self):
        client = Client()

        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)
