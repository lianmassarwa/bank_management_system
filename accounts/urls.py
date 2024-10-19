from django.urls import path
from .views import BankAccountCreateView, BankAccountCloseView

urlpatterns = [
    path('create/', BankAccountCreateView.as_view(), name='create-account'),
    #path('close/<int:pk>/', BankAccountCloseView.as_view(), name='close-account'),
]
