import requests
from test_APP.Common.Login_test import Login

# 查询资讯列表
def test_discoveryInformation():
    url = "http://192.168.101.102/api/user/app/discovery/information?index=1&size=20&sort=create_time"
    payload = {
        "index": 1,
        "size": 20,
        "sort": "create_time"
    }
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers=header, params=payload)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('查询')
    except:
        assert code != 0
        print('查询失败')


if __name__ == "__main__":
    test_discoveryInformation()
