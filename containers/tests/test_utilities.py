import unittest

from containers.utilities import (
    solution_cost,
    solve,
)


class TestSolutionCost(unittest.TestCase):
    def test_negative_load_should_return_absolute_value(self):
        self.assertEqual(solution_cost([5, 3, 2], 11), [1, 3])

    def test_positive_load_should_return_absolute_value(self):
        self.assertEqual(solution_cost([5, 4], 7), [2, 2])

    def test_equal_load_should_return_zero_value(self):
        self.assertEqual(solution_cost([4, 3, 2], 9), [0, 3])


class TestSolve(unittest.TestCase):
    tests = [
        {
            'params': [[5, 4, 3], 11],
            'output': [5, 3, 3]
        },
        {
            'params': [[4, 2], 11],
            'output': [4, 4, 4]
        },
        {
            'params': [[10, 5], 21],
            'output': [10, 10, 5]
        },
    ]

    def test_solutions(self):
        for test in self.tests:
            params = test['params']
            output = test['output']
            self.assertSetEqual(set(solve(*params)), set(output))
