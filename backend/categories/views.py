from django.shortcuts import render
from rest_framework import serializers, viewsets
from categories.serializers import CategorySerializer, CategoryListSerializer
from categories.models import Category
from transactions.models import Transaction
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
            queryset = Category.objects.all()
            serializer = CategoryListSerializer(queryset, many=True)
            return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def limit_exceeded(self, request, *args, **kwargs):
            queryset = Category.objects.all()
            filterArray = []
            for category in queryset:
                if category.is_limit_exceeded() == True: 
                        filterArray.append(category)

            serializer = CategoryListSerializer(filterArray, many=True)
            return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def limit_available(self, request, *args, **kwargs):
            queryset = Category.objects.all()
            filterArray = []
            for category in queryset:
                if category.is_limit_exceeded() == False: 
                        filterArray.append(category)
                        
            serializer = CategoryListSerializer(filterArray, many=True)
            return Response(serializer.data)