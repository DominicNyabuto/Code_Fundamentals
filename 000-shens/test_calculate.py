import unittest
from calculate import add

class test_calculate_app(unittest.TestCase):
    def test_positive_additions(self):
        self.assertEqual(add(4,6), 10)


if __name__ == '__main__':
    unittest.main()
    
