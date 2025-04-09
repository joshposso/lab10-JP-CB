# C:\Users\alpo7\PycharmProjects\lab10-JP-CB
# Partner 1: Josh Posso
# Partner 2: Callahan Bonifant
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5.0)
        self.assertEqual(div(5, 25), 5.0)
        self.assertAlmostEqual(div(2.5, 10), 4.0)

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-6, -8), 10.0)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)

    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################



    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    


# Do not touch this
if __name__ == "__main__":
    unittest.main()