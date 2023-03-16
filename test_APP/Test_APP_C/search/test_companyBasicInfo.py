import requests
import pytest
from test_APP.Common.Login_test import Login


class Test_search():
    # 查询公司工商信息
    def test_company_BasicInfo(self):
        url = "http://192.168.101.102/api/user/app/company/basic-info"
        header = {
            "token": Login().Login_sms_test_li()
        }
        payload = {
            "companyName": "海南强盛集团有限公司"
        }
        res = requests.get(url=url, headers=header, params=payload)
        print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print("成功")
        except:
            print("失败")


if __name__ == '__main__':
    Test_search().test_company_BasicInfo()
