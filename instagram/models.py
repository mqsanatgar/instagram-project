from django.conf import settings
from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserProfile(Base):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )
    username = models.CharField(max_length=65, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to="profiles/",
        null=True,
        blank=True,
    )
    # posts
    # comments
    # liked_posts


class Post(Base):
    user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    caption = models.TextField(
        max_length=10000,
        blank=True,
    )
    likes = models.ManyToManyField(
        to=UserProfile,
        related_name="liked_posts",
        # null=True,
        blank=True,
    )
    # images
    # comments


class Image(Base):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="images/")


class Comment(Base):
    user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField(max_length=1000, default="Hello")
