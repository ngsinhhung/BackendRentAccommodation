from django.shortcuts import render
from rest_framework import viewsets, status, generics, parsers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import UserSerializer, CommentSerializer, AccommodationSerializer, PostSerializer, ImageSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet, generics.ListAPIView, generics.CreateAPIView , generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(methods=['POST'], detail=False , url_path='register', url_name='register')
    def register_user(self, request):
        data = request.data
        role = data.role
        if role == 'HOST' or role == 'TENANT':
            if data.avatar_user is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(data=UserSerializer(data, context={'request': request}).data, status=status.HTTP_201_CREATED)

class AccommodationViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

class ImageViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class PostViewSet(viewsets.ModelViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
