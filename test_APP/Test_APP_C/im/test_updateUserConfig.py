# im即时通信——自动发送招呼语修改 开关

import requests
import json
from test_APP.Common.Login_test import Login


class Test_userconfig():
    def test_update_userconfig(self):
        url="http://192.168.101.102/api/user/app/im/update-userConfig/8"
        header={
            "token": Login().Login_sms_test(),
            "content-type":"application/json;charset=utf-8"
        }
        res = requests.put(url=url,headers=header)
        print(res.json())
        code = res.json()['code']
        data = res.json()['data']
        if code == 0 and data == True:
            print("修改成功")
        else:
            print("修改失败")





if __name__ == '__main__':
    Test_userconfig().test_update_userconfig()