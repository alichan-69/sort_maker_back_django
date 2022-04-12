from .response import create_api_response
from .exception import APIException


# キーの存在を確認
def check_exist_key(required_keys: list, post: dict):
    for key in required_keys:
        if key not in post:
            raise APIException(500, "{}がパラメータ内に存在しません".format(key))


FORMAT = {
    "user_id": {"type": str, "min": 1, "max": 255}
}

# キーに対するフォーマット（タイプ・文字数制限など）の確認


def check_value_format(post: dict):
    for key in post.keys():
        format = FORMAT[key]
        if format["type"] == str:
            # 文字列の場合
            if not (isinstance(post[key], str) and format["min"] <= len(post[key]) <= format["max"]):
                raise APIException(500, "{}のフォーマットが正しくありませんでした".format(key))
