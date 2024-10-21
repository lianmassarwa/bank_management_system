from rest_framework import serializers
from .models import Customer

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id' , 'username', 'email', 'phone_number','bank_username']
        read_only_fields = ['id', 'bank_username']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'phone_number': {'required': True},
        }

    def create(self, validated_data):
        # Create user without password first
        customer = Customer(**validated_data)
        customer.save()
        return customer
class SetPasswordSerializer(serializers.Serializer):
    bank_username = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=5)

    def validate(self, data):
        try:
            customer = Customer.objects.get(bank_username=data['bank_username'])
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Invalid bank username.")
        data['customer'] = customer
        return data

    def save(self):
        customer = self.validated_data['customer']
        customer.set_password(self.validated_data['password'])
        customer.save()
        return customer

from rest_framework import serializers
from django.contrib.auth import authenticate

class AuthTokenSerializer(serializers.Serializer):
    bank_username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        bank_username = attrs.get('bank_username')
        password = attrs.get('password')
        user = authenticate(username=bank_username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        attrs['user'] = user
        return attrs
