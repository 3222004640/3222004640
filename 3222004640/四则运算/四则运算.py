import sys
import argparse
import random
import math
from sympy import symbols, Eq, solve, simplify, Rational
from sympy.parsing.sympy_parser import parse_expr


# 生成一个只有两位操作数的算术表达式
def generate_integer_two(max_range):
    while True:
        number1 = random.randint(0, max_range - 1)
        number2 = random.randint(0, max_range - 1)
        list1 = [" + ", " - ", " * ", " / "]
        operator1 = random.choice(list1)
        if operator1 == " / " and number2 == 0:
            continue
        if operator1 == " - " and number2 > number1:
            number1, number2 = number2, number1
        list2 = [number1, operator1, number2]
        return list2


# 生成一个只有三位操作数的算术表达式
# 在生成两位操作数的算术表达式的基础上再随机生成一个操作符和一个数字
def generate_integer_three(max_range):
    while True:
        number3 = random.randint(0, max_range - 1)
        list1 = [" + ", " - ", " * ", " / "]
        operator2 = random.choice(list1)
        if operator2 == " / " and number3 == 0:
            continue
        else:
            list3 = generate_integer_two(max_range)
            list3.append(operator2)
            list3.append(number3)
            if calculation(list3) != "0":
                return list3


# 生成一个只有四位操作数的算术表达式
# 在生成三位操作数的算术表达式的基础上再随机生成一个操作符和一个数字
def generate_integer_four(max_range):
    while True:
        number4 = random.randint(1, max_range - 1)
        list1 = [" + ", " - ", " * ", " / "]
        operator3 = random.choice(list1)
        if operator3 == " / " and number4 == 0:
            continue
        else:
            list4 = generate_integer_three(max_range)
            list4.append(operator3)
            list4.append(number4)
            if calculation(list4) != "0":
                return list4


# 生成整数题目
def generate_questions(questions_number, max_range):
    f1 = open(r"Exercises.txt", mode="a", encoding="utf-8")
    f2 = open(r"Answers.txt", mode="a", encoding="utf-8")
    for i in range(questions_number):
        number = random.randint(1, 4)
        if number == 2:
            lst = generate_integer_two(max_range)
            f1.write("\n")
            f2.write("\n")
            f1.write(f"四则运算题目{i + 1}: ")
            f2.write(f"四则运算题目{i + 1}的答案: ")
            for item in lst:
                # print(item, end='')
                f1.write(str(item))
            f1.write(" =")
            if calculation(lst) is not None:
                f2.write(calculation(lst))

        elif number == 3:
            f1.write("\n")
            f2.write("\n")
            f1.write(f"四则运算题目{i + 1}: ")
            f2.write(f"四则运算题目{i + 1}的答案: ")
            lst = generate_integer_three(max_range)
            lst = insert(lst)
            for item in lst:
                # print(item, end='')
                f1.write(str(item))
            f1.write(" =")
            if calculation(lst) is not None:
                #  print(calculation(lst))
                f2.write(calculation(lst))
        elif number == 4:
            f1.write("\n")
            f2.write("\n")
            f1.write(f"四则运算题目{i + 1}: ")
            f2.write(f"四则运算题目{i + 1}的答案: ")
            lst = generate_integer_four(max_range)
            lst = insert(lst)
            for item in lst:
                f1.write(str(item))
            f1.write(" =")
            if calculation(lst) is not None:
                # print(calculation(lst))
                f2.write(calculation(lst))
        else:
            f1.write("\n")
            f2.write("\n")
            f1.write(f"四则运算题目{i + 1}: ")
            f2.write(f"四则运算题目{i + 1}的答案: ")
            lst = generate_decimal_two(max_range)
            for k in range(len(lst) - 1):
                f1.write(str(lst[k]))
            f1.write(" =")
            # print(str(lst[len(lst) - 1]))
            f2.write(str(lst[len(lst) - 1]))
    f1.close()
    f2.close()


# 插入括号
def insert(lst):
    parentheses_number = random.randint(0, 1)  # 插入括号的数目
    if parentheses_number == 1:
        parentheses_left_place = random.randint(0, len(lst) - 2)  # 左括号的插入位置
        while True:
            if parentheses_left_place % 2 == 0:
                break
            else:
                parentheses_left_place = random.randint(0, len(lst) - 2)
        parentheses_right_place = random.randint(parentheses_left_place + 4, len(lst) + 2)  # 右括号的插入位置
        while True:
            if parentheses_right_place % 2 == 0:
                break
            else:
                parentheses_right_place = random.randint(parentheses_left_place + 4, len(lst) + 2)
        lst.insert(parentheses_left_place, "(")
        lst.insert(parentheses_right_place, ")")
    return lst


# 生成真分数
def generate_decimal_two(max_range):
    number11 = random.randint(1, max_range)  # 分子
    number12 = random.randint(1, max_range)  # 分母
    # 判断生成的分数可不可以化成整数、能不能化简、是不是真分数、需不需要化成2'1/2的形式
    # 为了和运算符区别，将每一个分数都用括号括起来了
    if number11 > number12 and number11 % number12 != 0:
        integer_part1 = int(number11 // number12)
        remainder1 = int(number11 % number12)
        gcd1 = math.gcd(remainder1, number12)
        # fraction_part1 = (remainder1/gcd1)/(number12/gcd1)
        number1 = ["(", integer_part1, "'", int(remainder1 / gcd1), '/', int(number12 / gcd1), ")"]
        formatted_string1 = ''.join(map(str, number1))
    elif number11 < number12:
        remainder1 = int(number11 % number12)
        gcd1 = math.gcd(remainder1, number12)
        # fraction_part1 = (remainder1 / gcd1) / (number12 / gcd1)
        number1 = ["(", int(remainder1 / gcd1), "/", int(number12 / gcd1), ")"]
        formatted_string1 = ''.join(map(str, number1))
    else:
        number1 = int(number11 / number12)
        formatted_string1 = str(number1)
    # 生成另一个操作分数
    number21 = random.randint(1, max_range)  # 分子
    number22 = random.randint(1, max_range)  # 分母
    if number21 > number22 and number21 % number22 != 0:
        integer_part2 = int(number21 // number22)
        remainder2 = int(number21 % number22)
        gcd2 = math.gcd(remainder2, number22)
        number2 = ["(", integer_part2, "'", int(remainder2 / gcd2), "/", int(number22 / gcd2), ")"]
        formatted_string2 = ''.join(map(str, number2))
    elif number21 < number22:
        remainder2 = int(number21 % number22)
        gcd2 = math.gcd(remainder2, number22)
        # fraction_part2 = (remainder2 / gcd2) / (number22 / gcd2)
        number2 = ["(", int(remainder2 / gcd2), "/", int(number22 / gcd2), ")"]
        formatted_string2 = ''.join(map(str, number2))
    else:
        number2 = int(number21 / number22)
        formatted_string2 = str(number2)
    # 生成分数运算题目
    list1 = [" + ", " - ", " * ", " / "]
    operator1 = random.choice(list1)
    if operator1 == " - " and (number11 / number12) > (number21 / number22):
        operator1 = " + "
    list2 = [formatted_string1, operator1, formatted_string2]
    list3 = [number11, "/", number12, operator1, number21, "/", number22]
    result = calculation(list3)
    list2.append(result)
    return list2


# 计算两个操作数的结果
def calculation_two(lst):
    if lst[1] == " + ":
        result = lst[0] + lst[2]
        return str(result)
    elif lst[1] == " - " and lst[0] >= lst[2]:
        result = lst[0] - lst[2]
        return str(result)
    elif lst[1] == " * ":
        result = lst[0] * lst[2]
        return str(result)
    elif lst[1] == " / " and lst[2] != 0:
        if lst[0] % lst[2] == 0:
            result = int(lst[0] / lst[2])
            return str(result)
        else:
            if lst[0] > lst[2]:
                integer_part = int(lst[0] // lst[2])
                remainder2 = int(lst[0] % lst[0])
                gcd2 = math.gcd(remainder2, lst[2])
                number2 = [integer_part, "'", int(remainder2 / gcd2), "/", int(lst[2] / gcd2)]
                formatted_string2 = ''.join(map(str, number2))
                return formatted_string2
            else:
                remainder2 = int(lst[0] % lst[2])
                gcd2 = math.gcd(remainder2, lst[2])
                number2 = [int(remainder2 / gcd2), "/", int(lst[2] / gcd2), ]
                formatted_string2 = ''.join(map(str, number2))
                return formatted_string2
    else:
        return "0"


# 计算题目
def calculation(lst):
    expression = ''.join(map(str, lst))
    try:
        expr = parse_expr(expression)
        expr_simplified = simplify(expr)
        result = Rational(expr_simplified, 1)
    except (SyntaxError, TypeError, ValueError, NameError) as e:
        # 打印错误并返回None
        # print(f"Error parsing expression: {e}")
        return None
    # 如果是整数或者真分数，直接返回，如果是假分数，化成真分数再返回（返回的结果都是字符串）
    numerator = result.p  # 分子
    denominator = result.q  # 分母
    if result < 0:
        return "0"
    elif numerator % denominator == 0 or numerator < denominator:
        return str(result)
    else:
        integer_part = int(numerator // denominator)
        remainder2 = int(numerator % denominator)
        result = [integer_part, "'", remainder2, "/", denominator]
        formatted_string2 = ''.join(map(str, result))
        return formatted_string2


# 比较答案结果对错
def statistics_error():
    a = input("请输入要比较的文件路径：")
    f1 = open(a, mode="r", encoding="utf-8")
    f2 = open(r"Answers.txt", mode="r", encoding="utf-8")
    j = 0
    i = 0
    wrong = []
    correct = []
    for line_num, (line1, line2) in enumerate(zip(f1, f2), start=1):  # 按行读取文件
        # 去除每行可能存在的空白字符（如空格、换行符等）进行比较
        if line1.strip() != line2.strip():
            if line_num-1 != 0:
                wrong.append(line_num-1)
                j = j + 1
        else:
            if line_num - 1 != 0:
                correct.append(line_num-1)
                i = i + 1

    f3 = open(r"Grade.txt", mode="w", encoding="utf-8")
    # f3.write(correct_expression)
    f3.write(f"Correct: {i} ({', '.join(map(str, correct))})\n")
    f3.write(f"Wrong: {j} ({', '.join(map(str, wrong))})\n")


def main():
    parser = argparse.ArgumentParser(description='四则运算程序')
    parser.add_argument('-n', '--number', type=int, help='问题的数量')
    parser.add_argument('-r', '--range', type=int, help='问题的范围')
    args = parser.parse_args()
    questions_number = args.number if args.number is not None else 10
    max_range = args.range if args.range is not None else 10
    generate_questions(questions_number, max_range)
    print("题目和答案已经全部生成完毕")
    a = input("如果想对比答案，请输入1：")
    if a == '1':
        statistics_error()


if __name__ == "__main__":
    main()
