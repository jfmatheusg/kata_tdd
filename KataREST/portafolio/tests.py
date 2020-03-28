from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image
import json


# Create your tests here.
class PortafolioTestCase(TestCase):
    def test_portafolio_list(self):
        url = '/portfolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

