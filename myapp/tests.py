from django.test import TestCase
from django.urls import reverse

class LoginTestCase(TestCase):
    def setUp(self):
        self.login_url = reverse('login')

    def test_login_with_incorrect_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'wrong_username',
            'password': 'wrong_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")
