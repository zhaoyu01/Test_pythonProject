# c端拒绝简历邀请

import requests
import json
from test_APP.Common.Login_test import Login

class Test_send():
    def test_result_send(self):
        url="http://192.168.101.102/api/user/app/im/sendImMsg"
        header={
            "token": Login().Login_sms_test(),
            "content-type":"application/json; charset=utf-8"
        }
        payload={
            "SyncOtherMachine": 2,
            "From_Account": "C2097_test",
            "To_Account": "B3720_test",
            "MsgBody": [{
                "MsgType": "TIMCustomElem",
                "MsgContent": {
                    "Data": "{\"type\":\"B_C_ASK_RESUME_REJECT\"}",
                    "Desc": "null",
                    "Ext": "null",
                    "Sound": "null"
                }
            }],
            "SendMsgControl": ["NoUnread"]
        }
        res=requests.post(url=url,headers=header,data=json.dumps(payload))
        print(res.json())
        res.json()['code']
        if res.json()['code'] == 0:
            print('成功')
        else:
            print('失败')






if __name__ == '__main__':
    Test_send().test_result_send()