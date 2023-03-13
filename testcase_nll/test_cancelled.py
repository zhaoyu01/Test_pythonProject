import requests


class Test_Cancelled:
    def setup_class(self):
        # 声明域名
        self.host = "http://192.168.101.102"
        # 获取会话对象
        self.re = requests.session()
        payload = {
            "mobile": "18011111111",
            "code": "888888"
        }
        res = self.re.post(url=self.host + "/api/user/app/common/login/sms", json=payload)
        # 提取登录的token信息

        token = res.json()["data"]["token"]
        print(token)

        self.headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }

        # 用户申请注销账号

    def test_cancelled(self):
        payload1 = {
            "causes": ["在平台有多个账户"]
        }
        res1 = self.re.put(url=self.host + "/api/user/app/personal/setup/v2/cancelled", headers=self.headers,
                           json=payload1)
        print(res1.text, "**")
        code = res1.json()["code"]

        try:
            assert code == 0, "注销成功"
            print("注销成功")
        except:
            assert code != 0, "注销失败"

            print("注销失败")

        # 用户撤销注销申请

    def test_undo_cancelled(self):
        payload = {
            "value": "18011111111"
        }
        res = self.re.put(url=self.host + "/api/user/app/personal/setup/undo-cancelled", headers=self.headers,
                          json=payload)
        # print(res.text, "0")
        code = res.json()["code"]

        try:

            assert code == 0, "撤销成功"
            print("撤销成功")

        except:
            assert code != 0, "撤销失败"
            print("撤销失败")

    # 查看协议信息
    def test_agreement(self):
        res = self.re.get(url=self.host + "/api/user/app/personal/setup/agreement")
        code = res.json()["code"]
        try:

            assert code == 0, "查看协议成功"
            print("查看协议成功")

        except:
            assert code != 0, "查看协议失败"
            print("查看协失败")

    # 帮助与反馈

    def test_help_feedback(self):
        payload = {
            "message": "测试提交反馈接口"
        }
        res = self.re.post(url=self.host + "/api/user/app/personal/setup/help-feedback", json=payload)
        code = res.json()["code"]
        print(res.text)
        try:
            assert code == 0, "反馈成功"
            print("反馈成功")

        except:
            assert code != 0, "反馈失败"
            print("反馈失败")

        # 微信解绑

    def test_wei_xin(self):
        res = self.re.put(url=self.host + "/api/user/app/personal/setup/wei-xin")
        code = res.json()["code"]
        try:
            assert code == 0, "解绑成功"
            print("解绑成功")
        except:
            assert code != 0, "解绑失败"
            print("解绑失败")

    #         获取客服电话
    def test_phone(self):
        res = self.re.get(url=self.host + "/api/user/app/personal/setup/customer-phone")
        code = res.json()["code"]
        print(res.text)
        try:
            assert code == 0
            print("获取客服电话成功")
        except:
            assert code != 0
            print("获取客服电话失败")

    #     切换企业用户
    def test_member(self):
        res = self.re.post(url=self.host + "/api/user/app/personal/setup/switch/member")
        code = res.json()["code"]
        print(res.text)
        try:
            assert code == 0
            print("企业用户切换成功")
        except:
            assert code != 0
            print("企业用户切换失败")
