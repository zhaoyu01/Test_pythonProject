# im即时通信——获取当前沟通状态
import requests
import json
from test_APP.Common.Login_test import Login



class Test_chat_status():
    def test_chat_status(self):
        url="http://192.168.101.102/api/user/app/im/chat-status"
        header ={
            "content-type":"application/json; charset=utf-8",
            "token":Login().Login_sms_test()
        }
        payload={
            "jobId": 1407,
            "accountId": "3698",
            "source": "USER"
        }
        res=requests.post(url=url,headers=header,data=json.dumps(payload))
        print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print('成功')
        except:
            assert code != 0
            print('失败')


if __name__ == '__main__':
    Test_chat_status().test_chat_status()