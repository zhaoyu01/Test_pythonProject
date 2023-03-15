import requests

# 是否允许投递
def test_allowSend():
    url = "http://192.168.101.102/api/search/app/job/allow-send/560"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try :
        assert code == 0
        print("成功")
    except:
        print("失败")


