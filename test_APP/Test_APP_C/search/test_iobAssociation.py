import requests
import pytest
from test_APP.Common.Login_test import Login


class Test_search():

    # 下拉联想
    def test_jobAssociation(self):
        url = "http://192.168.101.102/api/search/app/job/association?keyword=JAVA"
        # header = {
        #     "token": Login.Login_sms_test01()
        # }
        payload = {
            "value": "java"
        }
        res = requests.get(url=url,
                           # headers=header,
                           data=payload)
        print(res.json())
        code = res.json()['code']
        assert code == 0
        # print('√')
        # assert code != 0
        # print('×')

        # try:
        #     assert code == 0
        #     print("√")
        # except:
        #     assert code != 0
        #     print("×")







# if __name__ == "__main__":
#     Test_search().test_iobAssociation()

