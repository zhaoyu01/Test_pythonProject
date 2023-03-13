# 提现余额到微信


import requests
import json
from test_APP.Common.Login_test import Login


class Test_money():
    def test_money(self):
        url="http://192.168.101.102/api/user/app/personal/money"
        header={
            "token": Login().Login_sms_test(),
            "content-type":"application/json; charset=utf-8"
        }
        payload={
            "amount": 5000
        }
        res=requests.post(url=url,headers=header,data=json.dumps(payload))
        print(res.json())
        if res.json()['code'] == 0:
            print('成功提现')
        else:
            print('提现失败')





if __name__ == '__main__':
    Test_money().test_money()
