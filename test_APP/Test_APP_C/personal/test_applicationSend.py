# c端用户申请发简历

import requests
import json
from test_APP.Common.Login_test import Login


class Test_send():
    def test_appliacation_send(self):
        url = "http://192.168.101.102/api/user/app/personal/im/application-send"
        header = {
            "token": Login().Login_sms_test(),
            "content-type": "application/json; charset=utf-8"
        }
        payload = {
            "jobId": 2470
        }

        res = requests.post(url=url, headers=header, data=json.dumps(payload))
        print(res.json())
        if res.json()['code'] == 0:
            print('成功')
        else:
            print('失败')


if __name__ == '__main__':
    Test_send().test_appliacation_send()
