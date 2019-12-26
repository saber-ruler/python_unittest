import os
import sys
# 添加路劲，导入模块
sys.path.append(os.getcwd())
import unittest
from HTMLTestRunner.python3x import HTMLTestReportCN
from public import sendEmail
from public import MyLog
from public import conf
import datetime


def allCase():
    case_dir = os.path.join(os.getcwd(), 'TestCase')
    # os.makedirs(case_dir)
    testcase = unittest.TestSuite()

    # discover方法筛选出来的用例，循环添加到测试套件中
    discover = unittest.defaultTestLoader.discover(
        case_dir, pattern='test*.py', top_level_dir=None)
    # print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
        # print(test_case)
    return testcase


def main():
    # allCase()
    version = datetime.datetime.now().strftime("%Y%m%d_%H")
    result_name = 'testresult_%s.html' % version
    log_name = MyLog.mylog().log_name()
    html_result_path = os.path.join(os.getcwd(), 'testResult')
    if not os.path.isdir(html_result_path):  # 判断是否存在文件，不存在则创建
        os.makedirs(html_result_path)

    html_result_file = os.path.join(html_result_path, result_name)
    with open(html_result_file, 'wb')as f:
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=f, title='自动化测试报告', description='用例执行情况：')
        runner.run(allCase())

    # 发送邮件
    sendEmail.send_mail(html_result_file, log_name)


if __name__ == '__main__':
    main()
