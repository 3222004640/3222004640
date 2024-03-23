import unittest
import random
from 四则运算 import generate_integer_two


class MyTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(0)
    def test_generate_with_normal_operators(self):
        operators = [" + ", " - ", " * ", " / "]
        for _ in range(10):  # 循环100次，以增加测试的随机性。
            result = generate_integer_two(10)  # 调用函数并获取结果。
            self.assertIn(result[1], operators, "Operator should be one of +, -, *, or /.")  # 断言运算符应该在定义的列表中。
            self.assertGreaterEqual(result[0], 0, "First number should be non-negative.")  # 断言第一个数字应该是非负的。
            self.assertLess(result[0], 10, "First number should be less than max_range.")  # 断言第一个数字应该小于max_range。
            self.assertGreaterEqual(result[2], 0, "Second number should be non-negative.")
            self.assertLess(result[2], 10, "Second number should be less than max_range.")

    def tearDown(self):
        random.seed(None)


if __name__ == '__main__':
    unittest.main()
