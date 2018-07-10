import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.illegal_input('ABCi'), True)
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
        self.assertEqual(checkout_solution.checkout('HHHH'), 40)
        self.assertEqual(checkout_solution.checkout('HHHHH'), 45)
        self.assertEqual(checkout_solution.checkout('HHHHHH'), 55)

        self.assertEqual(checkout_solution.checkout('HHHHHHHHHH'), 80)
        self.assertEqual(checkout_solution.checkout('HHHHHHHHHHHHHHHHHHHH'), 160)
        self.assertEqual(checkout_solution.checkout('HHHHHHHHHHHHHHHHHHHHH'), 170)
        self.assertEqual(checkout_solution.checkout('HHHHHHHHHHHHHHHHHHHHHHHHH'), 205)

        self.assertEqual(checkout_solution.checkout('K'), 80)
        self.assertEqual(checkout_solution.checkout('KK'), 150)
        self.assertEqual(checkout_solution.checkout('KKK'), 230)
        self.assertEqual(checkout_solution.checkout('KKKK'), 300)

        self.assertEqual(checkout_solution.checkout('NN'), 80)
        self.assertEqual(checkout_solution.checkout('NNN'), 120)
        self.assertEqual(checkout_solution.checkout('NNNNM'), 160)
        self.assertEqual(checkout_solution.checkout('NNMNM'), 135)

        self.assertEqual(checkout_solution.checkout('NNMNNNNN'), 280)
        self.assertEqual(checkout_solution.checkout('MMMMNNN'), 165)
        self.assertEqual(checkout_solution.checkout('PPPP'), 200)
        self.assertEqual(checkout_solution.checkout('PPPPP'), 200)

        self.assertEqual(checkout_solution.checkout('PPPPPPPPPPP'), 450)
        self.assertEqual(checkout_solution.checkout('QQ'), 60)
        self.assertEqual(checkout_solution.checkout('QQQ'), 80)
        self.assertEqual(checkout_solution.checkout('QQQQ'), 110)

        self.assertEqual(checkout_solution.checkout('QQQQQQ'), 160)
        self.assertEqual(checkout_solution.checkout('QQQQQQQQQ'), 240)
        self.assertEqual(checkout_solution.checkout('QQQQQQQQQQ'), 270)
        self.assertEqual(checkout_solution.checkout('UUU'), 120)

        
        self.assertEqual(checkout_solution.checkout('VV'), 90)

        self.assertEqual(checkout_solution.checkout('VVV'), 130)
        self.assertEqual(checkout_solution.checkout('VVVV'), 180)
        self.assertEqual(checkout_solution.checkout('VVVVV'), 220)
        self.assertEqual(checkout_solution.checkout('VVVVVV'), 260)

if __name__ == '__main__':
    unittest.main()
