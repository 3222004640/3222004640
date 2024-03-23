import unittest
import random
from sympy import parse_expr, simplify, Rational
from 四则运算 import generate_integer_three
from 四则运算 import calculation


class MyTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(0)

    def test_generate_integer_three(self):
        max_range = 10
        for _ in range(100):  # 运行多次测试
            result_list = generate_integer_three(max_range)

            # 确保生成的列表包含5个元素
            self.assertEqual(len(result_list), 5)
            self.assertTrue(all(isinstance(num, int) for num in result_list[::2]))
            self.assertTrue(all(isinstance(op, str) for op in result_list[1::2]))
            expression_result = calculation(result_list)

            # 确保计算没有错误，且结果不为"0"
            self.assertTrue(expression_result is not None, "Calculation failed")
            self.assertNotEqual(expression_result, "0", "Result should not be zero")

if __name__ == '__main__':
    unittest.main()
