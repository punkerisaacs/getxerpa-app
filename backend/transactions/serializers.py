from rest_framework import serializers
from transactions.models import Transaction
from categories.serializers import CategorySerializer
 
# Serializers define the API representation.
class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    categoryObject = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Transaction
        fields = ['description', 'date', 'amount', 'category', 'categoryObject', 'ignore']

class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['hour', 'description', 'amount', 'date', 'ignore']