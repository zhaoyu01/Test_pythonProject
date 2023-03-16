import requests
from test_APP.Common.Login_test import Login

# 搜索b端某个账号下的信息（公司，与您匹配信息）AppJobSearchByAccountVO
def test_byAccount_job():
    url = "http://192.168.101.102/api/search/app/job/job/by-account"
    header = {
        "Content-Type": "application/json",
        "token": Login().Login_sms_test_li()
    }
    payload = {
        "accountId": 3732
    }
    res = requests.get(url, headers=header, params=payload)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('查询成功')
    except:
        assert code != 0
        print('查询失败')


# 搜索b端某个账号下的信息（职位）AppJobSearchByAccountVO
def test_byAccount_allJob():
    url = "http://192.168.101.102/api/search/app/job/all-job/by-account?accountId=3732"
    header = {
        "Content-Type": "application/json",
        "token": Login().Login_sms_test_li()
    }
    payload = {
        "accountId": 3732
    }
    res = requests.get(url, headers=header, params=payload)
    print(res.json())



if __name__ == "__main__":
    test_byAccount_job()
    test_byAccount_allJob()