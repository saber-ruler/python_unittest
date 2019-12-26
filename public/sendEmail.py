from email.mime.text import MIMEText  # 发送邮件正文
from email.mime.multipart import MIMEMultipart  # 发送邮件附件
from email.header import Header
import smtplib
try:
    from . import conf
except ImportError as e:
    import conf
try:
    from . import MyLog
except ImportError as e:
    import MyLog
import datetime
import os


def Log():
    return MyLog.mylog().log()


def send_mail(file_result, file_log, **conf_data):
    conf_data = conf.confClass().conf_info()
    smtpserver = "smtp.qq.com"  # 发件服务器
    port = 465  # 端口
    # sender = "1419401663@qq.com"  # 发送端
    # psw = "qcwmcnynfrehbahc"  # 密码/授权码
    # receiver = "1419401663@qq.com"  # 接收端

    sender = conf_data['qq.send.email'][0]  # 发送端
    psw = conf_data['qq.send.password'][0]  # 密码/授权码
    receiver = conf_data['qq.recv.email']  # 接收端

    Log().info('QQreceiver: %s' % ','.join(receiver))
    #=========编辑邮件内容=========
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = ','.join(receiver)   # 收件人（多个人情况用逗号隔开）
    msg["subject"] = "自动化测试报告"  # 主题

    # 正文
    mail_body = '本次测试报告，请查收附件'
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)  # 挂起

    # 自动化测试结果
    f = open(file_result, 'rb')
    result_body = f.read()
    f.close()
    # 日志
    f1 = open(file_log, 'rb')
    flog = f1.read()
    f1.close()

    version = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    # 附件
    att = MIMEText(result_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="TestResult_%s.html"' % version  # 定义附件名称
    att2 = MIMEText(flog, "base64", "utf-8")
    att2["Content-Type"] = "application/octet-stream"
    # 定义附件名称
    att2["Content-Disposition"] = 'attachment; filename="TestLog_%s.log"' % version
    msg.attach(att)  # 挂起
    msg.attach(att2)  # 挂起

    #=========发送邮件=========
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()  # 关闭


if __name__ == '__main__':
    path1 = os.path.join(os.path.dirname(os.getcwd()),
                         'testResult\\testresult.html')
    path2 = os.path.join(os.path.dirname(os.getcwd()),
                         'testResult\\testresult.html')
    send_mail(path1, path2)
