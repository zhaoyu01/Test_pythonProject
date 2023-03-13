import pytest
import os


# import commands
# pytest main方法执行命令跑框架内测试用例
# if __name__=="__main__":
pytest.main(['--alluredir=reports'])
# pytest.main(['--report=.report.html',
#                 '--title=ZTCSBG',
#                 '--tester=测试员',
#                 '--desc=报告描述信息',
#                 '--template=2'])

# 调取CMD命令执行allure插件，生成报告
#  os.system(python demo.py)
# cmd = os.system('cd: .\zhaoyu\pythonProject1 && allure serve sports')

cmd = "allure serve reports"
tmp = os.popen(cmd)
res = tmp.read()
print(tmp)
tmp.close()

# cmd = "curl -s \"127.0.0.1:7070/api/v3/column/m.id,m.ip?m.sr.id=sls-backend-server.FuxiServiceSlsShennongWorker%23\"|grep m.ip|head -n 1 |awk '{print $2}'"
# dockervm_ip = commands.getoutput(cmd)
#print(dockervm_ip)

# result = os.popen('命令')
# res = result.read()

