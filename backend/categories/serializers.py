from rest_framework import serializers
from categories.models import Category
from transactions.serializers import TransactionSerializer

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'limit', 'totalAmount', 'transactionCount', 'spent', 'available']

class CategoryListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'limit', 'totalAmount', 'transactionCount', 'spent']