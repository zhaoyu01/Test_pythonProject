import requests
from test_APP.Common.Login_test import Login

# 智能消息-职位消息
def test_smartJob():
    url = "http://192.168.101.102/api/user/app/message/message/smart-job"
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers=header)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('成功')
    except:
        assert code != 0
        print('失败')
