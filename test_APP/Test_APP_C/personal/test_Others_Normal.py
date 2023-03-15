import requests

from test_APP.Common.Login_test import Login


# 查看自己的简历

class Test_Others_Normal():
    def test_others_normal(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/default/resume"
        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)
        code = res.json()["code"]
        try:
            assert code == 0
            print("查找成功")
        except:
            assert code != 0
            print("查找失败")


if __name__ == '__main__':

    Test_Others_Normal().test_others_normal()
