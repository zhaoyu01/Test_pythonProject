import requests

# APP 短信登录接口
class Login:

    def Login_sms_test(self):
        url = "http://192.168.101.102/api/user/app/common/login/sms"
        payload = {
            "mobile": 15444444444,
            "code": 888888
        }
        res = requests.post(url, json=payload)
        try:
            assert res.json()['code'] == 0
            print(res.json())
            return res.json()['data']['token']
        except:
            assert res.json()['code'] != 0
            print('登录失败请查看原因')


    def Login_sms_test01(self):
        url = "http://192.168.101.102/api/user/app/common/login/sms"
        payload = {
            "mobile": 15100000000,
            "code": 888888
        }
        res = requests.post(url, json=payload)
        try:
            assert res.json()['code'] == 0
            print(res.json())
            return res.json()['data']['token']
        except:
            assert res.json()['code'] != 0
            print('登录失败请查看原因')



    # 密码登录
    def Login_psd_test(self):

        url = "http://192.168.101.102/api/user/app/common/login/password"
        payload = {
            "mobile": 15444444444,
            "password": "a123456"
        }
        res = requests.post(url, json=payload)
        try:
            assert res.json()['code'] == 0
            print(res.json(), '登录成功')
            return res.json()['data']['token']
        except:
            assert res.json()['code'] != 0
            print('登录失败请查看原因')

    #B端用户登录
    def test_Blogin_sms(self):
        url = "http://192.168.101.102/api/member/app/auth/member/login/sms"
        payload = {
            "mobile": 15444444444,
            "code": "888888"
        }
        res = requests.post(url, json=payload)
        try:
            assert res.json()['code'] == 0
            print(res.json(), '登录成功')
            return res.json()['data']['token']

        except:

            assert res.json()['code'] != 0
            print('登录失败请查看原因')


if __name__ == '__main__':
    Login().test_Blogin_sms()
    Login().Login_sms_test01()
