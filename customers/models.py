from django.db import models
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length= 128 ,default='default_password')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone_number']

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)