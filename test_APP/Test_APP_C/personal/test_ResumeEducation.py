import requests

from test_APP.Common.Login_test import Login


# 学历下拉
class Test_Resume_Education():
    def test_resume_education(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/education"
        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)
        code = res.json()["code"]
        try:
            assert code == 0
            print("学历下拉查看成功")
        except:
            assert code != 0
            print("学历下拉查看失败")


if __name__ == '__main__':
    Test_Resume_Education().test_resume_education()
