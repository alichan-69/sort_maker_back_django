from .serializer import UserSerializer, SortSerializer, SortItemSerializer, LikeSerializer
from .models import User, Sort, SortItem, Like
from rest_framework import viewsets, mixins

from common.response import create_api_response
from common.exception import APIException
from common.auth import authenticate_register_user
from common.operate_instance import delete_instance

import traceback


def create_sort(self, request):
    print('hello')


def destroy_sort(self, request, pk):

    # ソートを削除する
    delete_instance(Sort, "id", pk)

    # ソートアイテムを削除する
    delete_instance(SortItem, "sort", pk)

    # お気に入りを削除する
    delete_instance(Like, "sort", pk)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SortViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

    def create(self, request):
        try:
            body = request.data
            authenticate_register_user(self, body)
            create_sort(self, request)
            return create_api_response(200, "OK")
        except APIException as e:
            return create_api_response(e.status_code, e.message)
        except Exception as e:
            return create_api_response(500, traceback.format_exc())

    def destroy(self, request, pk=None):
        try:
            body = request.data
            authenticate_register_user(self, body)
            destroy_sort(self, request, pk)
            return create_api_response(200, "OK")
        except APIException as e:
            return create_api_response(e.status_code, e.message)
        except Exception as e:
            return create_api_response(500, traceback.format_exc())


class SortItemViewSet(viewsets.ModelViewSet):
    queryset = SortItem.objects.all()
    serializer_class = SortItemSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
