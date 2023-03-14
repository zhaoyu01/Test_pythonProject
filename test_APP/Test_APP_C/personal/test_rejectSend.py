# c端用户拒绝 b端用户发简历邀请

import requests
import json
from test_APP.Common.Login_test import Login


class Test_send():
    def test_reject_send(self):
        url="http://192.168.101.102/api/user/app/personal/im/reject-send"
        header={
                "token": Login().Login_sms_test(),
                "content-type":"application/json; charset=utf-8"
        }
        payload={
            "jobId": 1866
        }
        res=requests.put(url=url,headers=header,data=json.dumps(payload))
        print(res.json())
        try:
            assert res.json()['code'] == 0 and res.json()['data'] == True
            print('发送成功')
        except:
            assert res.json()['code'] != 0
            print('发送失败',res.json()['msg'])


if __name__ == '__main__':
    Test_send().test_reject_send()