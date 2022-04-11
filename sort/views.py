from .serializer import SortSerializer
from .models import Sort
from rest_framework import viewsets, mixins

from common.response import create_api_response
from common.validation import check_exist_key, check_str_out_of_range
from common.format import date_format

import datetime


class SortViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

    def destroy(self, request, pk=None):
        body = request.data

        # ポストされたデータの必須キーの存在チェック
        required_keys = ["user_id"]
        check_exist_key(required_keys, body)

        # ポストされたデータを変数に格納
        b_user_id = body["user_id"]

        # その他データベースに登録する値を変数に格納
        delete_flg = True
        update_date = date_format(datetime.datetime.now())

        # バリデーション
        check_str_out_of_range(b_user_id, 1, 255)

        return create_api_response(200, "OK")
