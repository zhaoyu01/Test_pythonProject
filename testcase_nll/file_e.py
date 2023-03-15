import smtplib
import email.mime.text
import email.mime.multipart

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email(filelist, content=""):
    smtpHost = 'smtp.qq.com'  # 139邮箱SMTP服务器
    sendAddr = '448204492@qq.com'
    password = 'lhakvszfvxkabjjc'  # 163邮箱,则为授权码
    receiver = '13835348871@139.com'
    subject = "邮件标题"
    content = '正文内容'

    msg = MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = receiver
    msg['Subject'] = subject

    txt = MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)  # 添加邮件正文

    # 添加附件,传送filelist列表里的文件
    filename = ""
    i = 0
    for file in filelist:
        i = i + 1
        filename = file
        # print(str(i),filename)
        part = MIMEApplication(open(filename, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)

    server = smtplib.SMTP(smtpHost, 25)  # SMTP协议默认端口为25
    # server.set_debuglevel(1)  # 出错时可以查看

    server.login(sendAddr, password)
    server.sendmail(sendAddr, receiver, str(msg))
    print("\n" + str(len(filelist)) + "个文件发送成功")
    server.quit()