from django.urls import path
from .views import CustomerCreateView, CreateTokenView  # Adjust according to your view

urlpatterns = [
    path('create/', CustomerCreateView.as_view(), name='create-customer'),
    path('token/', CreateTokenView.as_view(), name='token'),
]
