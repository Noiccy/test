import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('asd'.upper(),'ASD')

if __name__ == '__main__':
    unittest.main()
