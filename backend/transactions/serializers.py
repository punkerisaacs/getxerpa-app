from rest_framework import serializers
from transactions.models import Transaction
from categories.serializers import CategorySerializer
 
# Serializers define the API representation.
class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Transaction
        fields = ['description', 'date', 'amount', 'category', 'ignore']

class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['monthName', 'description', 'amount', 'date']