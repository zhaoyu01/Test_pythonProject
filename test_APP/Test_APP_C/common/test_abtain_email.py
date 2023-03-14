# 获取邮箱验证码
import requests
from test_APP.Common.Login_test import Login


class Test_Obtain_Email:
    def test_obtain_email(self):
        url = "http://192.168.101.102/api/user/common/verify/email?email=138353488711111@139.com"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token":Login().Login_sms_test()
        }
        payload = {
            "email": "448204492@qq.com"
        }
        res = requests.get(url=url, headers=headers, json=payload)
        code = res.json()["code"]
        print(res.json())
        if code == 0:
            print("绑定成功")
        else:
            print("绑定失败")


if __name__ == "__main__":
    Test_Obtain_Email().test_obtain_email()
