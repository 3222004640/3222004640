import unittest
import random
from 四则运算 import generate_decimal_two
from 四则运算 import calculation
import re

class MyTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(0)

    def test_generate_decimal_two(self):
        max_range = 10
        for _ in range(100):
            result_list = generate_decimal_two(max_range)
            self.assertEqual(len(result_list), 4)

if __name__ == '__main__':
    unittest.main()
