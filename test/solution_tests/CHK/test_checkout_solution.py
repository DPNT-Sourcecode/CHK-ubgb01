import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.illegal_input('ABCY'), True)
        self.assertEqual(checkout_solution.illegal_input('ABCD'), False)

    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout('EE'), 80)
        self.assertEqual(checkout_solution.checkout('EEEEBB'), 160)
        self.assertEqual(checkout_solution.checkout('EEBEBEB'), 190)
        self.assertEqual(checkout_solution.checkout('EEBEEBEEB'), 240)

        self.assertEqual(checkout_solution.checkout('EEBB'), 110)
        self.assertEqual(checkout_solution.checkout('BAB'), 95)
        self.assertEqual(checkout_solution.checkout('AAAA'), 180)
        self.assertEqual(checkout_solution.checkout('AEEC'), 150)
        
        self.assertEqual(checkout_solution.checkout('CDBEA'), 155)
        self.assertEqual(checkout_solution.checkout('AAAAA'), 200)
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('BBBBB'), 120)
        self.assertEqual(checkout_solution.checkout('BBBBBBBEE'), 215)
        
        self.assertEqual(checkout_solution.checkout('AAABBD'), 190)
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('AAAAAAA'), 300)
        self.assertEqual(checkout_solution.checkout('AAAAAAAA'), 330)
        
        self.assertEqual(checkout_solution.checkout('AAAAAAAAA'), 380)
        self.assertEqual(checkout_solution.checkout('BBBBBBBBB'), 210)
        self.assertEqual(checkout_solution.checkout('BBBBBBBBBEE'), 260)
        self.assertEqual(checkout_solution.checkout('AABBCDD'), 195)
        
        self.assertEqual(checkout_solution.checkout('AAAAABCC'), 270)
        self.assertEqual(checkout_solution.checkout('AABbCDDea'), -1)

        self.assertEqual(checkout_solution.checkout('F'), 10)
        self.assertEqual(checkout_solution.checkout('FF'), 20)
        self.assertEqual(checkout_solution.checkout('FFF'), 20)
        self.assertEqual(checkout_solution.checkout('FFB'), 50)
        self.assertEqual(checkout_solution.checkout('FFFF'), 30)
        self.assertEqual(checkout_solution.checkout('FFFFF'), 40)
        self.assertEqual(checkout_solution.checkout('FFFFFF'), 40)
        self.assertEqual(checkout_solution.checkout('FFFFFFFF'), 60)
        self.assertEqual(checkout_solution.checkout('FFFFFFFFF'), 60)
        self.assertEqual(checkout_solution.checkout('FFFFFFFFFF'), 70)
        self.assertEqual(checkout_solution.checkout('FFEEBEEFFFFF'), 210)


if __name__ == '__main__':
    unittest.main()
