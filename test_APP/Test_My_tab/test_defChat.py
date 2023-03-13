# im即时通信——设置默认聊天配置   招呼语更换
import requests
import json
from test_APP.Common.Login_test import Login





class Test_defchat():
    def test_defchat(self):
        url ="http://192.168.101.102/api/user/app/im/defChat"
        header={
            "token":Login().Login_sms_test(),
            "content-type" : "application/json; charset=utf-8"
        }
        payload={
            "configId": 22,
            "content": "您好，可以聊一下么",
            "type": "GREETING"
        }
        res=requests.post(url=url,headers=header,data=json.dumps(payload))
        print(res.json())
        code = res.json()['code']
        if code == 0:
            print('配置成功')
        else:
            print('配置失败')


if __name__ == "__main__" :
    Test_defchat().test_defchat()

