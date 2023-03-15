import requests
import pytest


# 下拉联想（搜职位）
def test_jobAssociation():
    url = "http://192.168.101.102/api/search/app/job/association"
    payload = {
        "keyword": "测试"
    }
    res = requests.get(url, params=payload)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print("成功")
    except:
        print("失败")