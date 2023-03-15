import requests

from test_APP.Common.Login_test import Login


# 身份的下拉查看

class Test_Resume_Identity():
    def test_resume_identity(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/identity"
        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)


if __name__ == '__main__':
    Test_Resume_Identity().test_resume_identity()
