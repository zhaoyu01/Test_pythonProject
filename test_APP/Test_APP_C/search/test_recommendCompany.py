import requests
import pytest



# class Test_search():
# 加推公司
def test_recommendCompany():
    url = "http://192.168.101.102/api/search/app/company/recommendCompany"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print("成功")
    except:
        print("失败")