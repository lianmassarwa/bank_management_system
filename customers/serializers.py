from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import check_password

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'phone_number']
        read_only_fields = ['id']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'phone_number': {'required': True},
            'password': {
                'write_only': True,
                'min_length': 5
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Remove password from validated_data
        customer = Customer(**validated_data)
        customer.set_password(password)  # Hash the password
        customer.save()
        return customer

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')


        #user = authenticate(email=email, password=password)

        try:
            user = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid credentials.')

        attrs['user'] = user  # Store the user object
        return attrs