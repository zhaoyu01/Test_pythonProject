import requests

from test_APP.Common.Login_test import Login


# 职位类型下拉

class Test_Position_Type():
    def test_position_type(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/position-type"
        heasers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()

        }
        res = requests.get(url=url, headers=heasers)
        print(res.text)
        code = res.json()["code"]
        try:
            assert code == 0
            print("职位类型下拉成功")
        except:
            assert code != 0
            print("职位类型下拉失败")


if __name__ == '__main__':
    Test_Position_Type().test_position_type()
