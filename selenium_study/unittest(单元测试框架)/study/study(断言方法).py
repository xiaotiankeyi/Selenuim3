import unittest

class Test(unittest.TestCase,):
    def setUp(self):
        num = input('please input number:')
        self.num = int(num)

    def test_case(self):
        '''判断是否相等 a = b'''
        self.assertEqual(self.num, 10, msg='your input is not number')
        '''判断是否不相等'''
        self.assertNotEqual(self.num, 34, msg="test failed")

    def test_case2(self):
        a = 'hello'
        b = 'hello world'
        '''判断 a 是在 b 中,或是 b 包含 a '''
        self.assertIn(a, b, msg='test failed')

        '''判断 a 不在 b 中,或是 b 不包含 a'''
        self.assertNotIn(b, a, msg='test failed')


    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)