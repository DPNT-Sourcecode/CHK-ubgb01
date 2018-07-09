import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.illegal_input('ABCY'), True)
        self.assertEqual(checkout_solution.illegal_input('ABCD'), False)

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout('EEBB'), 95)
        self.assertEqual(checkout_solution.checkout('BAB'), 95)
        self.assertEqual(checkout_solution.checkout('AAAA'), 180)

        self.assertEqual(checkout_solution.checkout('AEEC'), 120)
        self.assertEqual(checkout_solution.checkout('CDBEA'), 155)
        self.assertEqual(checkout_solution.checkout('AAAAA'), 200)
 
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('BBBBB'), 120)
        self.assertEqual(checkout_solution.checkout('AAABBD'), 190)

        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('AAAAAAA'), 300)
        
        self.assertEqual(checkout_solution.checkout('AAAAAAAAA'), 380)
        self.assertEqual(checkout_solution.checkout('AABBCDD'), 195)
        self.assertEqual(checkout_solution.checkout('AAAAABCC'), 270)
        self.assertEqual(checkout_solution.checkout('AABbCDDea'), -1)


if __name__ == '__main__':
    unittest.main()
