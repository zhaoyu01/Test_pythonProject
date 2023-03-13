import pytest
import os
from test_APP import clear

pytest.main(['--alluredir=reports'])
# pytest.main(['--report=.report.html',
#                 '--title=ZTCSBG',
#                 '--tester=测试员',
#                 '--desc=报告描述信息',
#                 '--template=2'])

# 执行reports 文件清除
print(clear.ret)

cmd = "allure serve reports"
tmp = os.popen(cmd)
res = tmp.read()
print(tmp)
tmp.close()
