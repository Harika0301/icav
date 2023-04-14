from django.test import TestCase,Client

from django.contrib.auth.models import User
from django.urls import reverse


class LoginTests(TestCase):
    def setUp(self):
        self.url = reverse('login_api')
        self.client = Client()
        self.user = User.objects.create_user(
            username = 'testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_login_success(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('csv_import'))

    def test_login_failure(self):
       
        response = self.client.post(self.url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid email or password')
       