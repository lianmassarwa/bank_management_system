from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer

class CustomerAPITests(APITestCase):

    def test_create_customer(self):
        data = {
            'username': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123',
            'phone_number': '1234567890'
        }
        response = self.client.post('/api/customers/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_customer(self):
        Customer.objects.create_user(username='Jane Doe', email='jane@example.com', password='password123')
        response = self.client.post('/api/customers/token/', {'email': 'jane@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_login(self):
        response = self.client.post('/api/customers/token/', {'email': 'nonexistent@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
