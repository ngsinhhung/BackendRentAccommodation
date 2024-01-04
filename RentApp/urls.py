from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('accommodations', AccommodationViewSet, basename='accommodations')
router.register('post', PostViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls))
]