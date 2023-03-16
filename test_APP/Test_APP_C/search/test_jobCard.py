import requests
from test_APP.Common.Login_test import Login

# 职位卡片
def test_jobCard():
    url = "http://192.168.101.102/api/search/app/job/card"
    header = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
         "token": Login().Login_sms_test_li()
    }
    payload = {
        "accountId": 3732,
        "id": 1208
    }
    res = requests.get(url, headers=header
                       , params=payload
                       )
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('成功')
    except:
        assert code != 0
        print('失败')




# 根据职位id查询对应职位卡片

 # /api/search/app/job/card/{id}