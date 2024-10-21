from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer

class CustomerAPITests(APITestCase):

    def test_register_customer(self):
        data = {
            'username': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890'
        }
        response = self.client.post('/api/customers/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('bank_username', response.data)

    def test_set_password(self):
        customer = Customer.objects.create(username='John Doe', email='john@example.com', phone_number='1234567890')
        # Set bank_username if it's automatically generated in your Customer model
        # For example:
        customer.bank_username = "some_unique_username"  # Make sure to set the bank_username if necessary
        customer.save()

        data = {
            'bank_username': customer.bank_username,
            'password': 'password123'
        }
        response = self.client.post('/api/customers/set-password/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_customer(self):
        customer = Customer.objects.create(
            username='John Doe',
            email='john@example.com',
            phone_number='1234567890'
        )
        customer.bank_username = "unique_bank_username"
        customer.set_password('password123')
        customer.save()
        response = self.client.post('/api/customers/login/', {
            'bank_username': customer.bank_username,
            'password': 'password123'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
