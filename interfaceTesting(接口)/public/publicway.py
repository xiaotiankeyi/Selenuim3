import unittest

class Publicclass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('test start.....')

    @classmethod
    def tearDownClass(cls):
        print('test end quit.......')
