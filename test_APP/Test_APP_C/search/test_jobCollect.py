# 搜索——职位搜索——职位收藏/取消

import requests
import json
from test_APP.Common.Login_test import Login


class Test_collect():
    # 收藏
    def test_collect(self):
        url = "http://192.168.101.102/api/search/app/job/collect"
        header= {
            "token": Login().Login_sms_test(),
             "content-type":"application/json; charset=utf-8"
        }
        payload={
             "id": 1168,
             "collect": "true"
        }
        res=requests.post(url=url,headers=header,data=json.dumps(payload))
        print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print('收藏成功')
        except:
            assert code != 0
            print ('收藏失败')

        # 取消收藏
    def test_collect_not(self):
        url = "http://192.168.101.102/api/search/app/job/collect"
        header = {
            "token": Login().Login_sms_test(),
                # "ed9242518a6a41e4b7117a2ef6bffcad",
            "content-type": "application/json; charset=utf-8"
        }
        payload = {
            "id": 1168,
            "collect": "false"
        }
        res = requests.post(url=url, headers=header, data=json.dumps(payload))
        # print(res.json())
        code = res.json()['code']
        try:
            assert code == 0
            print('取消成功')


        except:
            assert code != 0
            print('取消失败')


if __name__ == '__main__' :
    Test_collect().test_collect()
    Test_collect().test_collect_not()


