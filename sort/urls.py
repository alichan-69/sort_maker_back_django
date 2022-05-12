from rest_framework import routers
from .views import UserViewSet, SortViewSet, SortItemViewSet, LikeViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sorts', SortViewSet)
router.register(r'sort_items', SortItemViewSet)
router.register(r'likes', LikeViewSet)
