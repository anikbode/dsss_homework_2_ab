import unittest
from math_quiz import random_integer_in_range, random_arithmetic_operator, arithmetic_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer_in_range(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_in_range(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_arithmetic_operator(self):
        for _ in range(1000):  # Test a large number of random values
            rand_op = random_arithmetic_operator()
            self.assertTrue(rand_op == '+' or rand_op == '-' or rand_op == '*',)

    def test_arithmetic_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (2, 5, '-', '2 - 5', -3),
                (5, -2, '*', '5 * -2', -10),
                (5, -2, '+', '5 + (-2)', 3),
                (5, 0, '*', '5 * 0', 0),
                (0, 0, '-', '0 - 0', 0),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = arithmetic_operation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
