import requests
from test_APP.Common.Login_test import Login

# 点赞/取消点赞资讯
def test_informationLike01():
    url = "http://192.168.101.102/api/user/app/discovery/information/like?id=65"
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers=header)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('点赞成功')
    except:
        assert code != 0
        print('不成功')


def test_informationLike02():
    url = "http://192.168.101.102/api/user/app/discovery/information/like?id=65"
    header = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers=header)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('取消成功')
    except:
        assert code != 0
        print('不成功')









if __name__ == "__main__":
    test_informationLike01()
    test_informationLike02()