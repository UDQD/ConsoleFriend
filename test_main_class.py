import unittest
from main_class import Mainclass


class Test_MainClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_vertex(self):
        self.assertEqual(Mainclass.get_vertex(Mainclass(), 'qweqweqwe'),
                         [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0])

        self.assertEqual(Mainclass.get_vertex(Mainclass(), 'ewrjkbcvlk jkb gdfx hjbh klj gh ds'),
                         [0, 3, 1, 2, 1, 1, 2, 3, 0, 4, 4, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0])