import pytest
import os
from test_APP import clear
from test_APP.Test_emali import emali_test
from test_APP.Test_emali import time
from test_APP.Test_emali.emali_test import email_ttt

# pytest.main(['--alluredir=reports'])
pytest.main(['--report=.report.html',
             '--title=众推职聘测试报告',
             '--tester=赵宇',
             '--desc=报告描述信息',
             '--template=2'])
print(clear.ret) # 执行reports 文件清除 需要时打开注释即可
email_ttt()

# cmd = "allure serve reports"
# tmp = os.popen(cmd)
# res = tmp.read()
# print(tmp)
# tmp.close()
