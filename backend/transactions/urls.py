from django.urls import include, path
from rest_framework.routers import DefaultRouter
from transactions.views import TransactionViewSet

router = DefaultRouter()
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
