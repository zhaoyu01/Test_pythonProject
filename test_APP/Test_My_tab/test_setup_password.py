# 查询是否有密码
import requests

from test_APP.Common.Login_test import Login


class Test_Setup_Password:
    def test_setup_password(self):
        url = "http://192.168.101.102/api/user/app/personal/setup/password"
        headers = {
            "token": Login().Login_sms_test(),
            "content_type": "application/json; charset=utf-8"

        }

        res = requests.get(url=url, headers=headers)
        print(res.json())


if __name__ == "__main__":
    Test_Setup_Password().test_setup_password()
