from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar_user = CloudinaryField('avatar', null = True, blank = True)
    phone = models.CharField(max_length=15, null=True, blank = True)
    class Role(models.TextChoices):
        TENANT = "TENANT", ('Người thuê')
        ADMIN = 'ADMIN', ('Quản trị viên')
        HOST = 'HOST', ('Chủ nhà')

    role = models.CharField(max_length=6, choices=Role.choices, default=Role.TENANT)

    def get_role(self) -> role:
        return self.Role(self.role)
    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey('User', on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='following')

class Accommodation(BaseModel):
    onwer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accommodation')
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number_of_people = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_verified = models.BooleanField(default=False, choices=[(True, 'Verified'), (False, 'Not Verified')])
    is_rented = models.BooleanField(default=False, choices=[(True, 'Rented'), (False, 'Not Rent')])

    def __str(self):
        return self.address

class Post(BaseModel):
    content = models.TextField()
    user_post = models.ForeignKey('User', on_delete=models.CASCADE, related_name='post')
    accommodation = models.ForeignKey('Accommodation', on_delete=models.CASCADE, related_name='post_accommodation')

    def __str__(self):
        return f'Post_{self.post.content}'

class Comment(models.Model):
    text = models.TextField()
    user_comment = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comment')
    created_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_comment', null=True, blank=True)

    def __str__(self):
        return f'{self.user_comment.username} comment {self.post.post_id}'


class Image(models.Model):
    image = CloudinaryField('image', null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post')
    accommodation = models.ForeignKey('Accommodation', on_delete=models.CASCADE, related_name='accommodation')
    def __str__(self):
        return f'Image_post_{self.post.id}'

class Notification(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='notifications')
    notice = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notify_{self.id}_of_{self.user.username}'
