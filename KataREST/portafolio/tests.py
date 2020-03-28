from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image, Portafolio
import json


# Create your tests here.
class PortafolioTestCase(TestCase):
    def test_portafolio_list(self):
        url = '/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_list_portafolios_count(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        image = Image.objects.create(name='nuevo', url='No', description='testImage', type='private')
        Portafolio.objects.create(name='nuevo', description='testImage', image=image, user=user_model)
        Portafolio.objects.create(name='nuevo2', description='testImage', image=image, user=user_model)

        url = '/portfolio/'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 3)