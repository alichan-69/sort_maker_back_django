from .response import create_api_response
from .exception import APIException


# キーの存在を確認
def check_exist_key(required_keys: list, post: dict):
    for key in required_keys:
        if key not in post:
            raise APIException(500, "{}がパラメータ内に存在しません".format(key))


FORMAT = {
    "user_id": {"type": str, "min": 1, "max": 255},
    "name": {"type": str, "min": 1, "max": 255},
    "description":  {"type": str, "min": 1, "max": 255},
    "item_names": {"type": list, "element_type": str, "min": 1, "max": 255}
}

# キーに対するフォーマット（タイプ・文字数制限など）の確認


def check_value_format(post: dict):
    for key in post.keys():
        format = FORMAT[key]
        if format["type"] == str:
            # 文字列の場合
            if not (isinstance(post[key], str) and format["min"] <= len(post[key]) <= format["max"]):
                raise APIException(500, "{}のフォーマットが正しくありませんでした".format(key))
        elif format["type"] == list:
            # リスト型の場合
            if not isinstance(post[key], list):
                raise APIException(500, "{}のフォーマットが正しくありませんでした".format(key))

            for el in post[key]:
                if format["element_type"] == str:
                    if not (isinstance(el, str) and format["min"] <= len(el) <= format["max"]):
                        raise APIException(
                            500, "{}のフォーマットが正しくありませんでした".format(key))
