from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    avatar_user = SerializerMethodField(source='avatar_user')
    def get_avatar_user(self, user):
        if user.avatar_user:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(user.avatar_user)
            return user.avatar_user.url
        return None
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'username', 'password', 'avatar_user', 'phone', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            # 'avatar_user': {'allow_null': False, 'required': True}
        }
    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()
        return user

class AccommodationSerializer(ModelSerializer):
    onwer = UserSerializer()
    class Meta:
        model = Accommodation
        fields = ['__all__']

class CommentSerializer(ModelSerializer):
    reply = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['text','user_comment', 'post', 'created_at', 'reply']

class PostSerializer(ModelSerializer):
    user_post = UserSerializer()
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['content', 'user_post', 'accommodation','image']
class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'created_at']
class NotificationsSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['__all__']