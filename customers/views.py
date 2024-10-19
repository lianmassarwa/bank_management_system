
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Customer
from .serializers import CustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
