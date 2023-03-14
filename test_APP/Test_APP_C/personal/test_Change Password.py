

# 修改密码

import requests
import json
from test_APP.Common.Login_test import Login


def test_change_password():
    url = "http://192.168.101.102/api/user/app/personal/setup/change-password"
    headers = {
        "token": Login().Login_sms_test(),
        "content-type": "application/json; charset=utf-8"
    }
    # 再次运行需要修改密码
    payload = {
        "oldPassword": "a123456",
        "newPassword": "a000023"
    }
    res = requests.put(url=url, headers=headers, data=json.dumps(payload))
    print(res.text)
    code = res.json()['code']
    if code == 0:
        print('修改成功')
    else:

        print('修改失败')


if __name__ == '__main__':
    test_change_password()
