from django.contrib import admin
from RentApp.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Accommodation)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Notification)

