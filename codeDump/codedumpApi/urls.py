from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FileViewSet, FileVersionViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'file', FileViewSet)
router.register(r'fileVersion', FileVersionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
