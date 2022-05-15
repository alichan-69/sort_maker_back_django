from sort.models import User

from common.validation import check_exist_key, check_value_format
from .exception import APIException
# ユーザー認証


def authenticate_user(post: dict):
    # ポストされたデータの必須キーの存在チェック
    required_keys = ["user_id"]
    check_exist_key(required_keys, post)

    post = {
        "user_id": post["user_id"]
    }

    # バリデーション
    check_value_format(post)

    instances = User.objects.filter(id=post["user_id"])
    if not len(instances):
        raise APIException(400, "ユーザー認証に失敗しました")

# ソートを登録したユーザーかの認証


def authenticate_register_user(self, post: dict):
    # ポストされたデータの必須キーの存在チェック
    required_keys = ["user_id"]
    check_exist_key(required_keys, post)

    # バリデーション
    check_value_format(post)

    instance = self.get_object()
    if not post["user_id"] == instance.user_id:
        raise APIException(400, "ソートを登録したユーザーではありません")
