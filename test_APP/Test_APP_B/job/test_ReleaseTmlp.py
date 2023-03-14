import requests
from test_APP.Common.Login_test import Login

# 查询 职位临时存储保存
def test_release():
    url = "http://192.168.101.102/api/member/app/job/release/temp"
    header = {
        "token": Login().test_Blogin_sms(),
    }
    res = requests.get(url=url, params=header)
    print(res.text)
    try:
        assert res.json()['code'] == 0
        print('执行成功')
    except:
        assert res.json()['code'] != 0
        print('执行失败')


if __name__ == '__main__':
    test_release()
