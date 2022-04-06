from rest_framework import routers
from .views import SortViewSet


router = routers.DefaultRouter()
router.register(r'sorts', SortViewSet)
