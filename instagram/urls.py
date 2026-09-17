from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet

router = DefaultRouter()
router.register("profiles", UserProfileViewSet, basename="user-profiles")
urlpatterns = router.urls

# instagram/profiles
# instagram/profile/me
# instagram/posts/
