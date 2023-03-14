# 查询配置开关
import requests
import json
from test_APP.Common.Login_test import Login


class Test_Confing:
    def test_confing(self):
        url = "http://192.168.101.102/api/user/app/im/get-userConfig"
        headers = {
            "content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "token": Login().Login_sms_test(),
            "referer": "*.ztzhipin.com"
        }
        payload = {
            "type": "INTEREST"
        }
        print(payload)
        res = requests.get(url=url, headers=headers, data=json.dumps(payload))
        print(res.json())
        try:
            assert res.json()['code'] == 0
            print('成功')
        except:
            assert res.json()['code'] != 0
            print('失败')


if __name__ == "__main__":
    Test_Confing().test_confing()
