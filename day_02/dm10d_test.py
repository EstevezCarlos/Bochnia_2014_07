import unittest
import dm10



class TestAdd(unittest.TestCase):
    def test_add_unittest(self):
        self.assertEqual(dm10.add(3,5),8)

def test_add_pytest():
    assert dm10.add(3,5) == 8

class TestAddPytest():
    @staticmethod
    def test_add_pytest():
        assert dm10.add(3,5) == 8