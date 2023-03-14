# 验证验证码是否正常

import requests
import json
from test_APP.Common.Login_test import Login


class Test_Verification_Code():
    def test_verification_code(self):
        url = "http://192.168.101.102/api/user/app/personal/setup/phone-verification-code"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": Login().Login_sms_test()
        }
        payload = {
            "mobile": "18035964746",
            "verificationCode": "888888"
        }

        res = requests.post(url=url, headers=headers, data=json.dumps(payload))
        code = res.json()["code"]
        print(res.json())
        if code == 0:
            print("验证码登录成功")
        else:
            print("验证码错误")


if __name__ == "__main__":
    Test_Verification_Code().test_verification_code()
