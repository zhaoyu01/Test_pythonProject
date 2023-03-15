import requests
from test_APP.Common.Login_test import Login


# 获取专业名联想查询
class Test_Major():
    def test_major(self):
        url = " http://192.168.101.102/api/user/app/personal/resume/major"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)

        code = res.json()["code"]

        try:
            assert code == 0
            print("获取联想成功")
        except:
            assert code != 0
            print("获取联想失败")


if __name__ == '__main__':
    Test_Major().test_major()
