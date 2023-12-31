from rest_framework import serializers
from categories.models import Category

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    limit = serializers.SerializerMethodField()

    def get_limit(self, obj):
        return float(obj.limit)

    class Meta:
        model = Category
        fields = ['id', 'name', 'totalAmount', 'transactionCount', 'limit', 'available', 'spent']

class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    limit = serializers.SerializerMethodField()

    def get_limit(self, obj):
        return float(obj.limit)

    class Meta:
        model = Category
        fields = ['id', 'name', 'totalAmount', 'limit', 'spent', 'transactionCount']