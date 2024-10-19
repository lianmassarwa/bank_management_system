import random
from django.db import models


def generate_account_number():
    return str(random.randint(10000000, 99999999))

class BankAccount(models.Model):
    account_number = models.CharField(max_length=20, unique=True, default=generate_account_number)
    account_holder = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='NIS')
    is_closed = models.BooleanField(default=False)
