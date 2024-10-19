from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import BankAccount

class BankAccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'account_number': '1234567890',
            'account_holder': 'John Doe',
            'balance': '1000.00',
            'currency':'NIS',
            'is_closed': False


        }

    def test_create_valid_bank_account(self):
        response = self.client.post('/api/accounts/create/', data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_close_account(self):
        url = f'/api/accounts/close/{self.account.id}/'
        response = self.client.patch(url)
        self.account.refresh_from_db()  # Refresh the instance to get the updated data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.account.is_closed)