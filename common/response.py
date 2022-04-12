from rest_framework.response import Response

# APIのレスポンスを作成する関数


def create_api_response(status_code: int, data: any):
    return Response(data=data, status=status_code)
