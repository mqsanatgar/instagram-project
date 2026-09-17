# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all().select_related("user")
    pagination_class = PageNumberPagination
