from rest_framework import serializers
from transactions.models import Transaction

# Serializers define the API representation.
class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'