import requests
from test_APP.Common.Login_test import Login


# 未读消息数
def test_noticeNumber():
    url = "http://192.168.101.102/api/user/app/message/message/notice-numbers"
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers=header)
    print(res.json())
    code = res.json()['code']
    all = res.json()['data']['all']
    print("所有未读消息数  " + str(all))

    try:
        assert code == 0
        print('接口成功')
    except:
        assert code != 0
        print('接口失败')