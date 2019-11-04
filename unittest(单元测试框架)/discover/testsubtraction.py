'''减法测试用例'''

from calculator import count
import unittest
from time import sleep, ctime

class Testaddition(unittest.TestCase):
    def setUp(self) -> None:
        print('test start')

    def test_case(self):
        j = count(23, 63)
        self.assertEqual(j.addition(), 86)

    def test_case2(self):
        g = count(43, 44)
        self.assertEqual(g.subtraction(), -1)


if __name__ == "__main__":
    unittest.main()
