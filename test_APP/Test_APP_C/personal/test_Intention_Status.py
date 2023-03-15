import requests

from test_APP.Common.Login_test import Login


# 当前状态下拉

class Test_Intention_Status():
    def test_intenion_status(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/intention-status"
        heasers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()

        }
        res = requests.get(url=url, headers=heasers)
        # print(res.text)
        code = res.json()["code"]
        try:
            assert code == 0
            print("下拉成功")
        except:
            assert code != 0
            print("下拉失败")


if __name__ == '__main__':
    Test_Intention_Status().test_intenion_status()
