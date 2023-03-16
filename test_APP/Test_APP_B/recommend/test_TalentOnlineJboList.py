import requests

from test_APP.Common.Login_test import Login


def Test_OlJobList(null=None):
    url = 'http://192.168.101.102/api/member/app/recommend/talent/online-job-list'
    header = {
        # 'token': Login().test_Blogin_sms()
        'token': 'e7c75215f84e4b73b8c42975f46f8758',
        'identity': 'PLANS'
    }
    res = requests.get(url=url, headers=header)
    print(res.text)
    data = res.json()['data']
    print(type(data))
    try:
        assert res.json()['code'] == 0 and res.json()['data'] != null
        print('在招职位列表查询成功')
    except Exception as e:
        assert res.json()['code'] != 0 or res.json()['data'] == null
        print('在招职位列表查询失败', 'Exception')


if __name__ == '__main__':
    Test_OlJobList()
