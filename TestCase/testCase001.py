import unittest
import os
import sys
# 添加路劲，导入模块
sys.path.append(os.path.dirname(os.getcwd()))
#import MyLog
from public import MyLog


def log():
    return MyLog.mylog().log()


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log().info('--开始测试--')

    @classmethod
    def tearDownClass(cls):
        log().info('--结束测试--')

    def setUp(self):
        log().info('开始单个测试用例')

    def tearDown(self):
        log().info('结束单个测试用例\n')

    def test_001(self):
        log().info('测试用例001')

    def test_002(self):
        log().info('测试用例002')

    def test_003(self):
        log().info('测试用例003')

    def test_004(self):
        data = self.assertEqual('1', '2', '测试失败0004')
        log().info(data)

    def test_005(self):
        log().info('测试用例005')


if __name__ == '__main__':
        # 运行所有test开头的方法
    unittest.main()
