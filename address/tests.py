from django.test import TestCase, Client

# Create your tests here.
from address.models import Address

class AddressTests(TestCase):

    def test_page(self):
        client = Client()

        address1 = Address.objects.create(postal_code = '12345',
                                          country = 'Ukraine',
                                          region = 'Kievska',
                                          district = '#13',
                                          street = 'Lenina',
                                          home = '100500'
                                          )

        response = client.get('/address/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ukraine")

        # response = client.get('/address/1/')
        # self.assertEqual(response.status_code, 404)

        response = client.get('/address/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ukraine")