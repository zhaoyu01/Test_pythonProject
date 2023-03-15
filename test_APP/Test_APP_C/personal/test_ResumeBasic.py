import requests

from test_APP.Common.Login_test import Login


# 在线简历-基本资料的查询

class Test_Resume_Basic():
    def test_resume_basic(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/basic"

        payload = {
            "baseInfoId": 11183
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers, params=payload)
        print(res.text)

        code = res.json()["code"]

        try:
            assert code == 0
            print("查询成功")
        except:
            assert code != 0
            print("查询失败")


if __name__ == '__main__':
    Test_Resume_Basic().test_resume_basic()
