import smtplib
import os
from log import log
from email.mime.text import MIMEText
from email.header import Header
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))

# SMTP 服务
mail_host = "smtp.163.com"
mail_user = os.environ.get('MAIL_USER')
mail_pass = os.environ.get('MAIL_PASS')

def send_email(sender, receivers, title, content):
    try:
        message = MIMEText(content, _subtype = 'html', _charset = 'utf-8')
        message['From'] = sender
        message['To'] =  ','.join(receivers)
        message['Subject'] = Header(title, 'utf-8')
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        log("邮件发送成功")
    except smtplib.SMTPException as err:
        log(f"Error: 无法发送邮件: {err}")
