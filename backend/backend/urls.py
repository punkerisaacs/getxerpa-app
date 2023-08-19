"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from categories.views import CategoryViewSet
from transactions.views import TransactionViewSet

# Routers provide an easy way of automatically determining the URL conf.
categoryRouter = routers.DefaultRouter()
categoryRouter.register(r'category', CategoryViewSet, basename='category')

# Nested router for chapters
transactionRouter = NestedDefaultRouter(categoryRouter, r'category', lookup='category')
transactionRouter.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(categoryRouter.urls)),
    path(r'api/', include(transactionRouter.urls)),
]
