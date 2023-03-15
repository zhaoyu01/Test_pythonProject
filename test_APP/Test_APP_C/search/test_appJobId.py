import requests

# 职位详情
def test_appJobId():
    url = "http://192.168.101.102/api/search/app/job/2570"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print("成功")
    except:
        print("失败")