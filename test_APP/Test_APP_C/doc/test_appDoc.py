import requests



# 根据分类编号获取文档历史版本列表  /api/user/app/doc/history/{catId}
def test_docHistory():
    url = "http://192.168.101.102/api/user/applet/doc/history/45"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('成功')
    except:
        assert code != 0
        print('失败')


# 根据分类编号获取最新的文档版本  /api/user/app/doc/new/{catId}
def test_docNew():
    url = "http://192.168.101.102/api/user/web/doc/new/45"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('成功')
    except:
        assert code != 0
        print('失败')


# 根据时间戳获取所有最新的文档版本
def test_docAllNew():
    url = "http://192.168.101.102/api/user/applet/doc/all/new?time=1678793770415"
    res = requests.get(url)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('成功')
    except:
        assert code != 0
        print('失败')



if __name__ == "__main__":
    test_docHistory()
    test_docNew()
    test_docAllNew()
