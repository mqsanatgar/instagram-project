from django.contrib import admin

from .models import Comment, Image, Post, UserProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Comment)
