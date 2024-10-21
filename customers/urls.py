from django.urls import path
from .views import CustomerRegisterView, SetPasswordView, LoginView

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='register'),
    path('set-password/', SetPasswordView.as_view(), name='set-password'),
    path('login/', LoginView.as_view(), name='login'),
]
