from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        User.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(reverse('login'), self.credentials)  # Replace 'login' with your login URL name
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertRedirects(response, reverse('home')) # Replace 'home' with your redirect URL name

    def test_login_invalid_username(self):
        self.credentials['username'] = 'invaliduser'
        response = self.client.post(reverse('login'), self.credentials) # Replace 'login' with your login URL name
        self.assertEqual(response.status_code, 200)  # Stays on login page
        self.assertContains(response, "Please enter a correct username and password.")

    def test_login_invalid_password(self):
        self.credentials['password'] = 'invalidpassword'
        response = self.client.post(reverse('login'), self.credentials) # Replace 'login' with your login URL name
        self.assertEqual(response.status_code, 200)  # Stays on login page
        self.assertContains(response, "Please enter a correct username and password.")

    def test_login_empty_credentials(self):
        response = self.client.post(reverse('login'), {}) # Replace 'login' with your login URL name
        self.assertEqual(response.status_code, 200)  # Stays on login page

    def test_logout(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('logout')) # Replace 'logout' with your logout URL name
        self.assertEqual(response.status_code, 302) # Redirect after logout
        self.assertRedirects(response, reverse('login')) # Replace 'login' with your redirect URL name

