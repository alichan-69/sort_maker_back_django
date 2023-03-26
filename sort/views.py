from .serializer import UserSerializer, SortSerializer, SortItemSerializer, LikeSerializer
from .models import User, Sort, SortItem, Like
from rest_framework import viewsets, mixins

from common.validation import check_exist_key, check_value_format
from common.response import create_api_response
from common.exception import APIException
from common.auth import authenticate_user, authenticate_register_user
from common.operate_instance import delete_instance

import traceback


def create_sort(self, request):
    post = request.data

    # ポストされたデータの必須キーの存在チェック
    required_keys = ["name", "description", "item_names"]
    check_exist_key(required_keys, post)

    # バリデーション
    check_value_format(post)

    # ソートを登録する
    sort = Sort(
        name=post["name"], description=post["description"], user_id=post["user_id"])
    sort.save()

    # ソートアイテムを登録する
    # for item_name in post["item_names"]:
    #     item_instance = SortItem.get


def destroy_sort(pk):

    # ソートを削除する
    delete_instance(Sort, "id", pk)

    # ソートアイテムを削除する
    delete_instance(SortItem, "sort", pk)

    # お気に入りを削除する
    delete_instance(Like, "sort", pk)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        print(repr(request))
        return create_api_response(200, "OK")


class SortViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

    def create(self, request):
        try:
            authenticate_user(request)
            create_sort(self, request)
            return create_api_response(200, "OK")
        except APIException as e:
            return create_api_response(e.status_code, e.message)
        except Exception as e:
            return create_api_response(500, traceback.format_exc())

    def destroy(self, request, pk=None):
        try:
            authenticate_user(request)
            authenticate_register_user(self, request)
            destroy_sort(pk)
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
