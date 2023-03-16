import requests
from test_APP.Common.Login_test import Login


def test_MemberSave():
    url = "http://192.168.101.102/api/member/app/auth/info/save"
    header = {
        "token": Login().test_Blogin_sms()
    }
    payload = {
        "contact": "李白",
        "companyName": "北京三元食品股份有限公司",
        "business": [40],
        "type": "PRODUCT",
        "scale": "1~9人",
        "scaleId": 3,
        "cityId": 1101,
        "city": "北京",
        "companyContactType": "吧"
    }
    res = requests.post(url=url, headers=header, params=payload)
    print(res.json())
    try:
        assert res.json()['code'] == 0
        print('企业资料修改成功')
    except:
        assert res.json()['code'] != 0
        print('资料修改失败')
    finally:
        assert res.json()['code'] == 1
        print('信息输入有误')

test_MemberSave()
