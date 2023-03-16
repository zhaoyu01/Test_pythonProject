import requests
from test_APP.Common.Login_test import Login


# 资讯详情

def test_informationId():
    url = "http://192.168.101.102/api/user/app/discovery/information/65"
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url,headers=header)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('查询')
    except:
        assert code != 0
        print('查询失败')


if __name__ == "__main__":
    test_informationId()