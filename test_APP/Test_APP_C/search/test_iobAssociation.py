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

    def test_jobAssociation_applet(self):
        url = "http://192.168.101.102/api/search/applet/job/association?keyword=java"
        # payload = {
        #     "keyword": "java"
        # }
        res = requests.get(url=url
                           # , data=payload
                           )
        print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print("成功")
        except:
            print("失败")



if __name__ == "__main__":
    Test_search().test_jobAssociation()
    Test_search().test_jobAssociation_applet()


