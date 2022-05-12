from .serializer import SortSerializer, SortItemSerializer
from .models import Sort, SortItem
from rest_framework import viewsets, mixins

from common.response import create_api_response
from common.validation import check_exist_key, check_value_format
from common.format import format_date
from common.exception import APIException
from common.auth import authenticate_register_user

import datetime
import traceback


def destroy_sort(self, request, pk):
    body = request.data

    # ポストされたデータの必須キーの存在チェック
    required_keys = ["user_id"]
    check_exist_key(required_keys, body)

    # バリデーション
    check_value_format(body)

    # ポストされたデータを変数に格納
    b_user_id = body["user_id"]

    # その他データベースに登録する値を変数に格納
    delete_flg = True
    update_date = format_date(datetime.datetime.now())

    # ソートを削除する
    sort_instance = self.get_object()
    sort_instance.delete_flg = delete_flg
    sort_instance.update_date = update_date
    sort_instance.save()

    # ソートアイテムを削除する
    sort_item_instances = SortItem.objects.filter(sort=pk)
    for sort_item_instance in sort_item_instances:
        sort_item_instance.delete_flg = delete_flg
        sort_item_instance.update_date = update_date
        sort_item_instance.save()


class SortViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

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


class SortItemViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = SortItem.objects.all()
    serializer_class = SortItemSerializer
