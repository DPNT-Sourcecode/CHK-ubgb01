import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.illegal_input('ABCY'), True)

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout('AAAA'), 180)
        self.assertEqual(checkout_solution.checkout('AAAAA'), 230)
        self.assertEqual(checkout_solution.checkout('BBBBB'), 105)
        self.assertEqual(checkout_solution.checkout('AAABCCC'), 220)
        self.assertEqual(checkout_solution.checkout('AABBCDD'), 195)
        self.assertEqual(checkout_solution.checkout('AABbCDD'), -1)


if __name__ == '__main__':
    unittest.main()
