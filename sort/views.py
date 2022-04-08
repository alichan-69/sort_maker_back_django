from rest_framework import viewsets, mixins, permissions

from .models import Sort
from .serializer import SortSerializer


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            body = request.data
            b_user_id = body['user_id']
            return False
        return True


class SortViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer
    permission_classes = (UserPermission, )

    def perform_destroy(self, instance):
        instance.delete_flg = True
        instance.save
