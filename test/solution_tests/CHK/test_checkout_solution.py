import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.illegal_input('ABCY'), True)
        self.assertEqual(checkout_solution.illegal_input('ABCD'), False)

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout('BAB'), 95)
        self.assertEqual(checkout_solution.checkout('CDBA'), 115)
        self.assertEqual(checkout_solution.checkout('AAAA'), 180)
        self.assertEqual(checkout_solution.checkout('AAAAA'), 230)
        self.assertEqual(checkout_solution.checkout('BBBBB'), 120)
        self.assertEqual(checkout_solution.checkout('AAABBD'), 190)
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 260)
        self.assertEqual(checkout_solution.checkout('AAABCCC'), 220)
        self.assertEqual(checkout_solution.checkout('AABBCDD'), 195)
        self.assertEqual(checkout_solution.checkout('AABbCDD'), -1)


if __name__ == '__main__':
    unittest.main()
