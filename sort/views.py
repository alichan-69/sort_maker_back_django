from rest_framework import viewsets, mixins

from .models import Sort
from .serializer import SortSerializer


class SortViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

    def perform_destroy(self, instance):
        instance.delete_flg = True
        instance.save
