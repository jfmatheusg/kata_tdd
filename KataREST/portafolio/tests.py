from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image, Portafolio, CustomUser
import json


# Create your tests here.
class PortafolioTestCase(TestCase):
    def test_portafolio_list(self):
        url = '/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_list_portafolios_count(self):
        user_model = CustomUser.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        image = Image.objects.create(name='nuevo', url='No', description='testImage', type='private')
        Portafolio.objects.create(name='nuevo', description='testImage', image=image, user=user_model)
        Portafolio.objects.create(name='nuevo2', description='testImage', image=image, user=user_model)

        url = '/portafolio/'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 2)

    def test_create_user(self):
        response = self.client.post('/portafolio/addUser/', json.dumps(
            {"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5",
             "email": "test@test.com", "professional_profile": "ingeniero"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'testUser')


    def test_list_portafolios_public(self):
        user_model = CustomUser.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        image = Image.objects.create(name='nuevo', url='No', description='testImage', type='private')
        Portafolio.objects.create(name='nuevo', description='testImage', image=image, user=user_model, privacity='public' )
        Portafolio.objects.create(name='nuevo2', description='testImage', image=image, user=user_model, privacity='private' )

        url = '/portafolio/'
        response = self.client.get(url, {'username': 'test', 'privacity': 'public'})
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 1)