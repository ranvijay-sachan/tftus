from django.urls import path, include
from .views import SalesManViewSet, CustomerViewSet
from rest_framework.routers import DefaultRouter

ROUTER = DefaultRouter()
ROUTER.register(r'salesman', SalesManViewSet)
ROUTER.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('', include(ROUTER.urls))
]