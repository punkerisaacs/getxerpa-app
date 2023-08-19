from django.shortcuts import render
from rest_framework import serializers, viewsets
from transactions.serializers import TransactionSerializer
from transactions.models import Transaction

# ViewSets define the view behavior.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer