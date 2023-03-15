import requests

from test_APP.Common.Login_test import Login


# 所属行业的下拉

class Test_ResumeBusiness():
    def test_resume_business(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/business"
        heasers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()

        }
        res = requests.get(url=url, headers=heasers)
        print(res.text)
        code = res.json()["code"]
        try:
            assert code == 0
            print("所属行业下拉成功")
        except:
            assert code != 0
            print("所属行业下拉失败")


if __name__ == '__main__':
    Test_ResumeBusiness().test_resume_business()
