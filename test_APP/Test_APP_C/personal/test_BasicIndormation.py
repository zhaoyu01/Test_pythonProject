import requests
from test_APP.Common.Login_test import Login

# 在线简历保存/修改保存
class Test_Basic_Information():
    def test_basic_information(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/save-basic-information"
        payload = {
            "baseInfoId": 11185,
            "name": "李浩楠",
            "gender": "WOMEN",
            "birthday": "1960-01-01",
            "workDate": "2019-01-01",
            "type": "HR",
            "city": "广州",
            "cityCode": "4401",
            "mobile": "15444444444",
            "email": "18035964746@163.com",
            "isMine": "true"
        }
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": Login().Login_sms_test()
        }
        res = requests.post(url=url, headers=headers, json=payload)
        print(res.text)
        code = res.json()["code"]

        try:
            assert code == 0
            print("保存成功")
        except:
            assert code != 0
            print("保存失败")


if __name__ == '__main__':
    Test_Basic_Information().test_basic_information()
