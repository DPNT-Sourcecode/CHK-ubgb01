import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.illegal_input('ABCY'), True)

    # def test_checkout(self):
    #     self.assertEqual(checkout_solution.checkout(self.friend_name), )


if __name__ == '__main__':
    unittest.main()
