'''加法测试用例'''

from calculator import count
import unittest


class Testaddition(unittest.TestCase):
    def setUp(self) -> None:
        print('test start')

    def test_case(self):
        j = count(23, 6)
        self.assertEqual(j.addition(), 29)

    def test_case2(self):
        g = count(43, 76)
        self.assertEqual(g.subtraction(), -33)


if __name__ == "__main__":
    unittest.main()
