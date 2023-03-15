import requests


# 全局搜索（职位）
def test_appJob():
    url = "http://192.168.101.102/api/search/app/job/"
    payload = {
        "sort": "updateTime",
        "expenseType": "CHARGE",
        "index": 1,
        "size": 20
    }
    res = requests.get(url, data=payload)
    print(res.json())
    code = res.json()['code']
    assert code == 0

# 全局搜索
def test_appJobV1():
    url = "http://192.168.101.102/api/search/app/job/v1"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    assert code == 0

if __name__ == "__main__":
    test_appJob()
    test_appJobV1()