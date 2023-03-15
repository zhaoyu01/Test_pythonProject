import requests
from test_APP.Common.Login_test import Login


# 工作性质下拉
class Test_Resume_Educattion():
    def test_resume_educattion(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/nature"
        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers)
        code = res.json()["code"]

        try:
            assert code == 0
            print("工作性质下拉成功")
        except:
            assert code != 0
            print("工作性质下拉失败")


if __name__ == '__main__':
    Test_Resume_Educattion().test_resume_educattion()
