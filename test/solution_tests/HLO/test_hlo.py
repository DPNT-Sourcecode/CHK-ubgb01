import unittest

from solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def setUp(self):
        self.friend_name = 'John'

    def test_sum(self):
        output = hello_solution.hello(self.friend_name)
        self.assertEqual(output, 'Hello, {}!'.format(self.friend_name))


if __name__ == '__main__':
    unittest.main()
