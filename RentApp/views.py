from django.shortcuts import render
from rest_framework import viewsets, status, generics, parsers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import UserSerializer, CommentSerializer, AccommodationSerializer, PostSerializer, ImageSerializer
import cloudinary.uploader
# Create your views here.
class UserViewSet(viewsets.ModelViewSet, generics.ListAPIView, generics.CreateAPIView , generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(methods=['POST'], detail=False , url_path='register', url_name='register')
    def register_user(self, request):
        try:
            data = request.data
            role = request.data.get('role')
            avatar = request.data.get('avatar_user')

            if role in [User.Role.HOST, User.Role.TENANT] and not avatar:
                return Response({'error': 'Avatar user not found'}, status=status.HTTP_400_BAD_REQUEST)

            res = cloudinary.uploader.upload(data.get('avatar_user'), folder = 'avatar_user/')

            new_user = User.objects.create_user(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                phone = data.get('phone'),
                role = role,
                avatar_user=res['secure_url'],
            )
            return Response(data=UserSerializer(new_user, context={'request': request}).data, status=status.HTTP_201_CREATED)
        except:
            print("Error")

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
