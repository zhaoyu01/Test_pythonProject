import requests






# 根据分类编号获取最新的文档版本
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


if __name__ == "__main__":
    test_docNew()