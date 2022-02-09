import os
import time
import unittest
import smtplib
from BeautifulReport import BeautifulReport
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
suite = unittest.defaultTestLoader.discover("C:/Users/推广部/PycharmProjects/ruoyi_api/", "*ruoyi_order.py")
BeautifulReport(suite).report(description=u'用例执行情况', log_path="C:/Users/推广部/PycharmProjects/ruoyi_api/suite_demo/", filename="ruoyi_order_"+time.strftime("%Y-%m-%d %H_%M_%S"))
# 文件夹目录
path = "C:/Users/推广部/PycharmProjects/ruoyi_api/sunite_demo/"
# 获取文件夹中所有的文件(名)，以列表形式返回
lists = os.listdir(path)
print("未经处理的文件夹列表：\n %s \n"%lists)
# 按照key的关键字进行生序排列，lambda入参x作为lists列表的元素，获取文件最后的修改日期，
# 最后对lists以文件时间从小到大排序
lists.sort(key=lambda x:os.path.getmtime((path+"/"+x)))
# 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
file_new = os.path.join(path, lists[-1])
print("时间排序后的的文件夹列表：\n %s \n"%lists )
print("最新文件路径:\n%s"%file_new)

def smtp():
    fromaddr = '2148583859@qq.com'
    password = 'wijflxwqtatjecfc'
    toaddrs = ['2148583859@qq.com', '2327992376@qq.com']
    content = '1、OA客户订单相关接口''\r\n' \
              '2、查看测试报告请下载附件,浏览器打开html文件'
    textApart = MIMEText(content)
    imageFile = '测试报告模版.png'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    htmlFile = lists[-1]
    htmlApart = MIMEText(open(htmlFile, 'rb').read(), 'base64', 'utf-8')
    htmlApart.add_header('Content-Disposition', 'attachment', filename=htmlFile)
    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)
    m.attach(htmlApart)
    m['Subject'] = 'python接口自动化测试'
    m['From'] = '2148583859@qq.com'
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('邮件发送成功')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)

#if __name__ == '__main__':
    #smtp()
