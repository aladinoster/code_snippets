import unittest

from my_package.my_module import my_func


class TestMyModule(unittest.TestCase):

    def test_creation(self):
        my_func()
        self.assertEqual(1, 1)
