# 消息——消息标记已读

import requests
import json
from test_APP.Common.Login_test import Login


def test_message_read():
    url="http://192.168.101.102/api/user/app/message/message/read"
    header={
            "token": Login().Login_sms_test(),
            "content-type":"application/json; charset=utf-8"

    }
    payload={
        "all": "true"
    }
    res=requests.put(url=url,headers=header,data=json.dumps(payload))
    print(res.text)
    code = res.json()['code']
    data = res.json()['data']
    try:
        assert code == 0 and data == True
        print("标记已读")
    except:
        assert code != 0
        print("标记失败")



if __name__ == "__main__" :
    test_message_read()