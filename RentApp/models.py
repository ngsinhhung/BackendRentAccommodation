from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar_user = CloudinaryField('avatar', null = True)
    phone = models.CharField(max_length=15, null=True)
    date_joined = models.DateField(auto_now_add=True)
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Quản trị viên')
        HOST = 'HOST', _('Chủ nhà')
        TENANT = "TENANT", _('Người thuê')

    role = models.CharField(max_length=6, choices=Role.choices, default=Role.TENANT)

    def get_role(self) -> role:
        return self.Role(self.role)
    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey('User', on_delete=models.CASCADE, related_name='followerrr')
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='followinggg')

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

class Post(BaseModel):
    content = models.TextField()
    user_post = models.ForeignKey('User', on_delete=models.CASCADE, related_name='post')
    accommodation = models.ForeignKey('Accommodation', on_delete=models.CASCADE, related_name='post_accommodation')



class Image(models.Model):
    image = CloudinaryField('image', null = True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post