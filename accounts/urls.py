from django.urls import path
from .views import BankAccountCreateView, BankAccountCloseView , AccountView

urlpatterns = [
    path('', AccountView.as_view(), name='accounts-dblist'),
    path('create/', BankAccountCreateView.as_view(), name='create-account'),
    #path('close/<int:pk>/', BankAccountCloseView.as_view(), name='close-account'),
]
