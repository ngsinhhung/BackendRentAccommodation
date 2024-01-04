from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password", "avatar_user", "phone", "role"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()
        return user

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'created_at']

class AccommodationSerializers(ModelSerializer):
    onwer = UserSerializer()
    class Meta:
        model = Accommodation
        fields = ["__all__"]

class PostSerializers(ModelSerializer):
    user_post = UserSerializer()
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['content', 'user_post', 'accommodation', 'image']

    def get_image(self, obj):
        image = Image.objects.filter(post_id=obj.id)
        serializer = PostSerializers(image, many=True)

        return serializer.data


class CommentSerializers(ModelSerializer):
    reply = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['text','user_comment', 'post', 'created_at', 'reply']

    def get_reply(self, obj):
        reply = Comment.objects.filter(parent_comment=obj)
        serializer = CommentSerializers(reply, many=True)



class NotificationsSerializers(ModelSerializer):
    class Meta:
        model = Notification
        fields = ["__all__"]