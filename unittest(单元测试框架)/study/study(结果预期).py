import os,sys
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base)

from  no_use_unittest.one import count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')


    # @unittest.skip('直接跳过测试')
    def test_A(self):
        j = count(4, 8)
        self.assertEqual(j.count_digit(), 12)

    # @unittest.skipIf(3 > 2, '当条件为True时跳过测试')
    def test_B(self):
        l = count(4, 7)
        self.assertEqual(l.subtraction(), 3)

    # @unittest.skipUnless(3 > 2, '当条件为True时执行测试')
    def test_C(self):
        u = count(3, 78)
        self.assertEqual(u.count_digit(), 81)

    '''测试标记为失败'''
    # @unittest.expectedFailure
    def test_D(self):
        i = count(6, 10)
        self.assertEqual(i.subtraction(), 4)

    def tearDown(self):
        print('test end')

if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_D"))
    suite.addTest(TestCount("test_A"))
    suite.addTest(TestCount("test_B"))
    suite.addTest(TestCount("test_C"))


    #测试执行
    runner = unittest.TextTestRunner()
    runner.run(suite)

"""
unittest框架默认根据ASCLL码顺序加载测试用例,数字与字母的顺序为：0~~~9, A~~~Z
"""