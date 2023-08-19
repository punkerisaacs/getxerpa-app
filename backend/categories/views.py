from django.shortcuts import render
from categories.models import Category
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, action
from categories.serializers import CategorySerializer, CategoryListSerializer

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
        newCategories = []

        if 'exceeded' in request.GET:
                exceeded = request.GET.get('exceeded')
                for category in queryset:
                        if category.is_limit_exceeded() == int(exceeded): 
                                newCategories.append(category)
        else:
                newCategories = queryset

        serializer = CategoryListSerializer(newCategories, many=True)
        return Response(serializer.data) 