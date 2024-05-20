

import unittest


class DivisionTests(unittest.TestCase):
    def test_integer_division(self):
        result = 20 // 3
        self.assertEqual(result, 6, "Integer division should return the floor value")

    def test_normal_division(self):
        result = 20 / 3
        self.assertAlmostEqual(result, 6.6666666666666667, places=10, msg="Normal division should return the precise floating-point result")

    def test_division_coerces_to_float(self):
        one = 1
        three = 3
        self.assertTrue(type(one) == type(three))
        self.assertTrue(isinstance(one, int))
        self.assertTrue(isinstance(three, int))
        result = 1 / 3
        self.assertTrue(isinstance(result, float), msg="Division with integers results in a float")
        self.assertAlmostEqual(result, 0.3333333333333333, places=10, msg="Division with integers results in a correct answer")
    
    def test_almost_equal_three_repeating(self):
        result = 1.0 / 3.0
        self.assertAlmostEqual(result, 0.3333333333333333, places=10, msg="Floating-point values should be almost equal")
    
    def test_almost_equal_six_repeating(self):
        result = 2.0 / 3.0
        self.assertAlmostEqual(result, 0.6666666666666666, places=10, msg="Floating-point values should be almost equal")

    


if __name__ == "__main__":
    unittest.main()
