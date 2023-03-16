import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from test_APP.Test_emali.time import get_webserver_datetime
from testcase_nll.file_t import get_type_file


def email_ttt():
    # 设置发送邮箱服务器
    smptServer = 'smtp.qq.com'
    # 设置发送邮箱用户、密码或授权码（163和QQ需要的是授权码不是密码）
    user = '448204492'
    psword = 'lhakvszfvxkabjjc'
    # 发送邮箱
    sender = '448204492@qq.com'
    # 接收邮箱
    # receiver = ['li271050@163.com', '18035964746@163.com', 'li271050@163.com', '18035964746@163.com', 'shayuanjie@ztzhipin.com', 'lizhixiao@ztzhipin.com']
    receiver = ['13835348871@139.com']

    # 发送文件主题
    subject = '自动化测试报告'
    # 发送html格式的文件
    #print(str(fill().report_file_list())[1:-1])


    path = 'D:\zhaoyu\Test_pythonProject\\test_APP\\reports\\' + get_type_file()
    print(path, '发的邮件文件在这里')
    rrr = r'D:\zhaoyu\Test_pythonProject\test_APP\reports\.report.html'
    # path = os.getcwd() + r'D:\zhaoyu\Test_pythonProject\test_APP\reports\2023-03-14_15_49_33.report.html'
    # path = os.getcwd()
    # print(path)
    # 编写HTML类的邮箱正文
    file = open(path, 'rb')
    # print(file)
    f = file.read()
    file.close()
    msg = MIMEMultipart()
    # 实例化html文件
    html_part = MIMEText(f, 'base64', 'gb2312')  # 将html文件以附件的形式发送
    html_part['Content-Type'] = 'application/octet-stream'
    html_part.add_header('Content-Disposition', 'attachment', filename='测试报告.html')  # filename是指下载的附件的命名

    # 绑定到message里
    msg.attach(html_part)

    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    # msg['To'] = receiver
    msg['to'] = ','.join(receiver)

    # 创建发送邮箱服务对象
    smtp = smtplib.SMTP()
    # 连接发送邮件服务器
    smtp.connect(smptServer)
    # 登录邮箱，输入邮箱名，密码
    smtp.login(user, psword)
    # 发送邮件
    smtp.sendmail(sender, receiver, msg.as_string())
    print('邮件已发送')
    # 关闭邮箱对象
    smtp.quit()

if __name__ == '__main__':
    email_ttt()