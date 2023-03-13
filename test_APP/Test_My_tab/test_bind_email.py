# 绑定邮箱

import requests
import json
from test_APP.Common.Login_test import Login


class Test_Bind_Email():
    def test_bind_email(self):
        url = "http://192.168.101.102/api/user/app/personal/setup/bind-email"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": Login().Login_sms_test(),
        }
        payload = {
            "email": "18035964746@163.com",
            "dynamicCode": "9754"
        }

        res = requests.post(url=url, headers=headers, data=json.dumps(payload))
        code = res.json()["code"]
        print(res.json())
        if code == 0:
            print("绑定成功")
        else:
            print("绑定失败")


if __name__ == "__main__":
    Test_Bind_Email().test_bind_email()
