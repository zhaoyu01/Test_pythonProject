import requests



def test_applet_index():
    url = "http://192.168.101.102/api/search/applet/job/recommendCompany"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print("成功")
    except:
        print("失败")