

# 修改手机号
import requests

import json
from test_APP.Common.Login_test import Login

class Test_Mobile():
    def test_mobile(self):
        url = "http://192.168.101.102/api/user/app/personal/setup/mobile"
        headers = {
            "content-type": "application/json;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        payload = {
            "mobile": "18000001122",
            "verificationCode": "888888"
        }
        res = requests.put(url=url, headers=headers, data=json.dumps(payload))
        code = res.json()["code"]
        print(res.text)
        if code == 0:
            print("修改成功")
        else:
            print("修改失败")


if __name__ == "__main__":
    Test_Mobile().test_mobile()
