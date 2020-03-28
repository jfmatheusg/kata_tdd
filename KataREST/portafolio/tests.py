from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image, Portafolio, CustomUser
import json


# Create your tests here.
class PortafolioTestCase(TestCase):



    def test_list_portafolios_public(self):
        user_model = CustomUser.objects.create_user(username='test', password='kd8wke-DE34', first_name='test name',
                                              last_name='test last name', email='test@test.com')
        image = Image.objects.create(name='nuevo', url='No', description='testImage', type='private')
        Portafolio.objects.create(name='nuevo', description='testImage', image=image, user=user_model, private=False)
        Portafolio.objects.create(name='nuevo2', description='testImage', image=image, user=user_model, private=True)

        url = '/portafolio/'
        response = self.client.get(url, {'username': 'test', 'private': 'False'})
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 1)
