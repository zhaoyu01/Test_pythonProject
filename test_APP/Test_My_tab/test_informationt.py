import requests
import json
from test_APP.Common.Login_test import Login
from test_APP.Config import config_value


def Test_edit_information():
    # 输入 测试接口的URL
    url_coo = "http://192.168.101.102/api/user/app/personal/setup/info"

    # 登录抓包获取的头部
    header_coo = {
        "referer": "*.ztzhipin.com",
        "token": Login().Login_sms_test(),
        "sing": "EDA7CDAB2FF378459465EE1E8DD8D81A",
        "content-Type": "application/json; charset=utf-8"
    }
    # 基本信息修改
    payload_coo = {
        "nickName": config_value.name(),
        "gender": config_value.gender(),
        "headImage": config_value.pic(),
        "birthday": config_value.get_birthday(),
        "type": config_value.type_add(),
    }

    # print(payload_coo)
    res_coo = requests.put(url=url_coo, headers=header_coo, data=json.dumps(payload_coo))
    code = res_coo.json()['code']
    data = res_coo.json()['data']
    '''if code  == 0:
        print('修改成功') 
    else:
        print('修改失败')'''
    print(res_coo.json())
    try:
        assert code == 0 and data == True
        print('基本信息修改成功')
    except:
        assert code != 0
        print('基本信息修改失败')


if __name__ == '__main__':
    Test_edit_information()
'''    pytest.main([
        '--report=musen.html',
        '--title=ZT测试报告',
        '--tester=测试员',
        '--desc=报告描述信息',
        '--template=2'
                 ])'''
