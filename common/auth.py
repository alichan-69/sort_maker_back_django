from common.validation import check_exist_key, check_value_format
from .exception import APIException

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
