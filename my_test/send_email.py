import smtplib
from email.mime.text import MIMEText
from email.header import Header

# smtpserver='smtp.163.com'
#
# user='yxp0916@163.com'
# password='yxp045489'
#
# sender='yxp0916@163.com'
# receiver='402081019@qq.com'

subject='Web Selenium自动化测试报告'
content='<html><h1 style="color:red">我要自学sss网，自学成才！</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='yxp0916@163.com'
msg['To']='402081019@qq.com'

smtp=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp.helo(smtpserver)
# smtp.ehlo(smtpserver)
smtp.login('yxp0916@163.com','yxp045489')

print("Start send Email...")
smtp.sendmail('yxp0916@163.com','yxp0916@163.com',msg.as_string())
smtp.quit()
print("Start Email End!")