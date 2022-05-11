from rest_framework import routers
from .views import SortViewSet, SortItemViewSet


router = routers.DefaultRouter()
router.register(r'sorts', SortViewSet)
router.register(r'sort_items', SortItemViewSet)
