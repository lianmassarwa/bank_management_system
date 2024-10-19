from rest_framework import serializers
from .models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'account_number', 'account_holder', 'balance','currency' ,'is_closed']
        read_only_fields = ['id', 'account_number', 'is_closed']
