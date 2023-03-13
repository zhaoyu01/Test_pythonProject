# 个人中心——资产——领红包到推币

import requests
import json
from test_APP.Common.Login_test import Login

class Test_red_packet():
    def test_red_packet(self):
        url="http://192.168.101.102/api/user/app/personal/red-packet/71"
        header={
                "token": Login().Login_sms_test(),
                "content-type":"application/json; charset=utf-8"
        }
        res =requests.post(url=url,headers=header)
        print(res.json())





if __name__ == '__main__':
    Test_red_packet().test_red_packet()