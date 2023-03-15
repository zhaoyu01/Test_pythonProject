import requests
import pytest
from test_APP.Common.Login_test import Login


class Test_search():
    # 根据关键字全局搜索公司
    def test_companyPage(self):
        url = "http://192.168.101.102/api/search/app/company/company-page"
        # header = {
        #
        # }
        payload = {
            "keyword": "强盛建工集团",
            "index": 1,
            "size": 10
        }
        res = requests.get(url, params=payload)
        print(res.text)
        code = res.json()['code']
        assert code == 0

