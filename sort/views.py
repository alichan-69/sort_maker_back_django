from .serializer import SortSerializer
from .models import Sort
from rest_framework import viewsets, mixins

from common.response import create_api_response
from common.validation import check_exist_key, check_value_format
from common.format import date_format
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
    update_date = date_format(datetime.datetime.now())


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