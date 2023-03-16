import requests
from test_APP.Common.Login_test import Login

# 查询文档类型列表
def test_docDocumentCat():
    url = "http://192.168.101.102/api/user/applet/doc/documentCat"
    headers = {
        "token": Login().Login_sms_test_li()
    }
    res = requests.get(url, headers)
    print(res.json())
    code = res.json()['code']
    try:
        assert code == 0
        print('查询')
    except :
        assert code != 0
        print('失败')


if __name__ == "__main__":
    test_docDocumentCat()