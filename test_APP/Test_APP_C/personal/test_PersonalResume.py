import json

import requests
from test_APP.Common.Login_test import Login


# 删除简历信息
class Test_PersonalResume():
    def test_Personal_Resume(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/11117"
        payload = {
            "id": "11117"
        }
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.delete(url=url, headers=headers, data=json.dumps(payload))
        print(res.text)
        code = res.json()["code"]

        try:
            assert code == 0
            print("删除成功")
        except:
            assert code != 0
            print("删除失败")


if __name__ == '__main__':
    Test_PersonalResume().test_Personal_Resume()
