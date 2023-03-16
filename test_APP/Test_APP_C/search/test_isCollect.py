import requests
from test_APP.Common.Login_test import Login

# 判断当前职位是否收藏
def test_isCollect():
    url = "http://192.168.101.102/api/search/app/job/is-collect?jobId=2533"
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url=url, headers=header)
    print(res.json())
    code = res.json()['code']
    result = res.json()['data']['result']
    try:
        assert code == 0
        print("判断成功")
        try:
            assert result == True
            print("已收藏")
        except:
            assert result == False
            print("没有收藏")
    except:
            assert code != 0
            print("判断不出来")









