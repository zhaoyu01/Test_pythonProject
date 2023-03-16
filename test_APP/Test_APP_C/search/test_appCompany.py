import requests
import pytest
from test_APP.Common.Login_test import Login

class Test_search():
    # 全局搜索
    def test_appCompany01(self):
        url = "http://192.168.101.102/api/search/app/company?natureId=&businessId=&scaleId=&financingId=&index=1&size=20"
        header = {
            "token": Login().Login_sms_test_li()
        }
        res = requests.get(url=url,headers=header)
        print(res.text)
        code = res.json()['code']
        try:
            assert code == 0
            print("成功")
        except:
            print("失败")

    # 全局搜索
    def test_appCompany02(self):
        url = "http://192.168.101.102/api/search/app/company"
        header = {
            "token": Login().Login_sms_test_li()
        }
        payload = {
            "keyword": "强盛建工集团",
            "index": 1,
            "size": 3
        }

        res = requests.get(url=url,
                           headers=header,
                           data=payload)
        print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print("成功")
        except:
            print("失败")

    # 公司详情
    def test_appCompany03(self):
        url = "http://192.168.101.102/api/search/app/company/1666319565542"
        header ={
            "token": Login().Login_sms_test_li()
        }

        res = requests.get(url=url,headers=header)
        print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print("成功")
        except:
            print("失败")


if __name__ == "__main__":
    Test_search().test_appCompany01()
    Test_search().test_appCompany02()
    Test_search().test_appCompany03()