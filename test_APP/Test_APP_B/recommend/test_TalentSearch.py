from test_APP.Common.Login_test import Login
import requests


# 人才搜索
def Test_talentSearch():
    url = "http://192.168.101.102/api/member/app/talent/talent-pool/search"
    header = {
        'token': Login().test_Blogin_sms(),
        'identity': 'PLANS'
    }
    payload = {
        "index": 1,
        "size": 10,
        "keyword": "测试",

    }
    res = requests.post(url=url, headers=header, json=payload)
    print(res.text)
    try:
        assert res.json()['code'] == 0
        print('搜索正常')
    except:
        assert res.json()['code'] != 0
        print('搜索失败')


if __name__ == '__main__':
    Test_talentSearch()
