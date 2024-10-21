from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string

class Customer(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    bank_username = models.CharField(max_length=12, unique=True, blank=True, null=True)

    # Add related_name to prevent clashes with Django's auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_permissions',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'bank_username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def save(self, *args, **kwargs):
        if not self.bank_username:
            # Generate unique bank username
            self.bank_username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            while Customer.objects.filter(bank_username=self.bank_username).exists():
                self.bank_username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bank_username
