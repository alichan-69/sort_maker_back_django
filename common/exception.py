# APIステータスのクラス
class APIException(Exception):
    def __init__(self, status_code: int, message=""):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        n = int(self.status_code / 100)
        if n == 2:
            return "OK" + ": " + self.message
        elif n == 4:
            return "unauthrized" + ": " + self.message
        else:
            return "server error" + ": " + self.message
