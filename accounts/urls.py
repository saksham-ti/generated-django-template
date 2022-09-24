from rest_framework.routers import DefaultRouter

from .views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user-detail")
