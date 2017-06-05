# coding:utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import os

# 发送邮箱服务器
smtpserver = 'smtp.mxhichina.com'
# 发送邮箱用户名/密码
user = 'kim.zheng@91nuanyou.com'
password = 'xiaozheng_1829'
# 发送邮箱
sender = 'kim.zheng@91nuanyou.com'
# 接收邮箱
receiver = 'kim.zheng@91nuanyou.com', '272489037@qq.com'
# 发送主题
subject = '暖游上线-自动化测试报告-20160914'

sendfile = open('C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\2016-09-14 00_13_45result.html', 'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename = "2016-09-14 00_13_45result.html"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
