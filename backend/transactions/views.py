from django.shortcuts import render
from transactions.models import Transaction
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, action
from transactions.serializers import TransactionSerializer, TransactionListSerializer

# ViewSets define the view behavior.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs):
        queryset = Transaction.objects.filter(category_id = kwargs["category_pk"])
        serializer = TransactionListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = Transaction.objects.get(pk = kwargs["pk"], category_id = kwargs["category_pk"])
            serializer = self.get_serializer(queryset, many=False)
            return Response(serializer.data) 
        except Transaction.DoesNotExist:
            return Response({}) 