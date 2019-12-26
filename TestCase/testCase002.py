import unittest
import os
import sys
# 添加路劲，导入模块
sys.path.append(os.path.dirname(os.getcwd()))
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

    def test_006(self):
        log().info('测试用例006')

    def test_007(self):
        log().info('测试用例007')

    def test_008(self):
        log().info('测试用例008')

    def test_009(self):
        ex = Exception('执行用例抛出异常')
        raise ex
        log().info('测试失败009')


if __name__ == '__main__':
        # 运行所有test开头的方法
    unittest.main()
