import requests
from test_APP.Common.Login_test import Login

# 分页查询消息---推币/职位/系统
def test_messageList():
    url = "http://192.168.101.102/api/user/app/message/message/list?index=1&size=20&isRead="
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers=header)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('成功查询')
    except:
        assert code != 0
        print('查询失败')