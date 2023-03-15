import json

import requests
from test_APP.Common.Login_test import Login


class Test_Analysis():
    def test_analysis(self):
        url = "http://192.168.101.102/api/user/app/personal/resume/analysis"
        #  请求头

        headers = {
            "Content-Type": "multipart/form-data",
            "token": Login().Login_sms_test()
        }
        # 上传文件的参数
        # files = {
        #     "file": ("【Android开发工程师_北京】毛华伟 4年.pdf", open("D:\测试\简历附件\【Android开发工程师_北京】毛华伟 4年.pdf", "rb"), "application/octet-stream")
        # }
        files = {"files": open('D:\测试\简历附件\【Android开发工程师_北京】毛华伟 4年.pdf', 'rb')}

        res = requests.post(url=url, headers=headers, files=files)

        print(res.text)


if __name__ == '__main__':
    Test_Analysis().test_analysis()
