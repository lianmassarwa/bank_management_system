from rest_framework import generics
from rest_framework.views import APIView

from .models import BankAccount
from .serializers import BankAccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



class BankAccountCreateView(generics.CreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class AccountView(APIView):
    serializer_class = BankAccountSerializer

    def get(self, request):
        return Response({'message': 'List of accounts'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BankAccountCloseView(generics.UpdateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        # Get the account instance based on the primary key (pk) in the URL
        account = self.get_object()

        # Check if the account is already closed
        if account.is_closed:
            return Response({"detail": "This account is already closed."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the is_closed field to True
        account.is_closed = True
        account.save()

        return Response({"detail": "Account closed successfully."}, status=status.HTTP_200_OK)
