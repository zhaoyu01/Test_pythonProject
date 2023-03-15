import smtplib
import email.mime.text
import email.mime.multipart

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def get_type_file(keyword='.html'):  # 这里可以更改扩展名如.doc,.py,.zip等等
    # 打印当前的工作目录
    print('当前目录为：', r'D:\zhaoyu\Test_pythonProject\test_APP\reports')
    path = "D:/zhaoyu/Test_pythonProject/test_APP/reports"
    # 列举当前工作目录下的文件名
    files = os.listdir(path)
    keyword = keyword
    filelist = []
    i = 0
    for file in files:
        if keyword in file:
            i = i + 1
            print(i, file)
            filelist.append(file)

            return file


get_type_file()