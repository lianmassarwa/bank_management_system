from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Customer
from .serializers import CustomerRegistrationSerializer, SetPasswordSerializer, AuthTokenSerializer

class CustomerRegisterView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            customer = serializer.instance
            print(f"Customer registered with bank_username: {customer.bank_username}")  # Debugging info

            return Response({
                "id": customer.id,
                "bank_username": customer.bank_username,  # Return the generated bank_username
                "email": customer.email,
                "phone_number": customer.phone_number
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetPasswordView(generics.GenericAPIView):
    serializer_class = SetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password set successfully."})
        return Response(serializer.errors, status=400)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            # Return the token, bank_username, and user ID
            return Response({
                "token": token.key,
                "bank_username": user.bank_username,
                "id": user.id
            }, status=200)
        return Response(serializer.errors, status=400)
