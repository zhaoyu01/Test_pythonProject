import requests
from test_APP.Common.Login_test import Login


# 获取学校名联想查询
class Test_School():
    def test_school(self):
        url = " http://192.168.101.102/api/user/app/personal/resume/school"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)

        code = res.json()["code"]

        try:
            assert code == 0
            print("联想成功")
        except:
            assert code != 0
            print("联想失败")


if __name__ == '__main__':
    Test_School().test_school()
