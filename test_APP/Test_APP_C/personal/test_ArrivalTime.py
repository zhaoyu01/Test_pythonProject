import requests

from test_APP.Common.Login_test import Login


# 到岗时间下拉

class Test_Arrival_Time():
    def test_arrival_time(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/arrival-time"
        heasers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()

        }
        res = requests.get(url=url, headers=heasers)
        print(res.text)
        code = res.json()["code"]
        try:
            assert code == 0
            print("到岗下拉成功")
        except:
            assert code != 0
            print("到岗下拉失败")


if __name__ == '__main__':
    Test_Arrival_Time().test_arrival_time()
