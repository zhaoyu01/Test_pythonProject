import requests


# 小程序首页
def test_applet_index():
    url = "http://192.168.101.102/api/search/applet/job/index"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print("成功")
    except:
        print("失败")




def test_applet_newJob():
    url = "http://192.168.101.102/api/search/applet/job/new-job"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print("成功")
    except:
        print("失败")


if __name__ == '__main__':
    test_applet_index()
    test_applet_newJob()