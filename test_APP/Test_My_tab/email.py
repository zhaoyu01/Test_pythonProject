print("*************139邮箱形式*****************")
# 授权码： ***
# 接收邮件服务器：imap.139.com，使用SSL，端口号993
# 发送邮件服务器：smtp.139.com，使用SSL，端口号465


# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = '13835348871@139.com'  # 发件人邮箱账号
# my_sender = '448204492@qq.com'
my_pass = 'qaz123123'  # 发件人邮箱密码（139邮箱密码不需要授权，就是自己的登录密码）
my_user = '13835348871@139.com'  # 收件人邮箱账号

mail_msg = r'reports.\report.html'
# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>
# """


def mail():
    ret = True
    try:
        msg = MIMEText(mail_msg, 'plain', 'utf-8')  # 此处为仅填写文本数据
        # msg=MIMEText(mail_msg,'html','utf-8')      #需要发送html数据的时候用这种形式(139邮箱不能用，会被当成垃圾邮件退回)
        msg['From'] = formataddr(["13835348871", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Run等待", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "OFFer发放"  # 邮件的主题，也可以说是标题

        '''
        mail_host = 'smtp.qq.com'
        mail_user = '448204492'
        mail_pass = 'ikugditaanxnbjcg'
        sender = 'zhaoyu448204492@qq.com'
        receivers = ['448204492@qq.com']
        '''

        server = smtplib.SMTP_SSL("smtp.139.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e,'1')
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
