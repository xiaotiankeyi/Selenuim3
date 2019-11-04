import unittest

class Publicclass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('test start.....')

    @classmethod
    def tearDownClass(cls) -> None:
        print('test end quit.......')
