

# 获取基本信息
import requests
import json
from test_APP.Common.Login_test import Login


def test_infor():
    url = "http://192.168.101.102/api/user/app/personal/setup/info"
    headers = {
        "Content_Type": "application/json; charset=utf-8",
        "token": Login().Login_sms_test()

    }

    res = requests.get(url=url, headers=headers)

    print(res.json())


if __name__ == "__main__":
    test_infor()
