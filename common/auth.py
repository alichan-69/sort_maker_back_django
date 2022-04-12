from .exception import APIException

# ソートを登録したユーザーかの認証


def authenticate_register_user(self, post: dict):
    instance = self.get_object()
    if not post["user_id"] == instance.user_id:
        raise APIException(400, "ソートを登録したユーザーではありません")
