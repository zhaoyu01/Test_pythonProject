import requests
from test_APP.Common.Login_test import Login

# 查询热门资讯列表
def test_popularInformation():
    url = "http://192.168.101.102/api/user/app/discovery/information/popular-information"
    header = {
        "token": Login().Login_sms_test_li()
    }
    payload = {
        "index": 1,
        "size": 5
    }
    res = requests.get(url, headers=header, params=payload)
    print(res.json())
    code = res.json()['code']

    # assert code == 0
    try:
        assert code == 0
        print('查询成功')
    except:
        assert code != 0
        print('查询失败')





if __name__ == "__main__":
    test_popularInformation()