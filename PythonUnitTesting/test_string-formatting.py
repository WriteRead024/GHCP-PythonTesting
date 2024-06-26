from os import path
import unittest


class StringFormatting(unittest.TestCase):
    def test_f_string_interpolation(self):
        a, b = 1, 2
        self.assertEqual(f"{a} + {b} = {a + b}", "1 + 2 = 3")

    def test_format_method(self):
        a, b = 1, 2
        self.assertEqual("{0} + {1} = {2}".format(a, b, a + b), "1 + 2 = 3")

    def test_percent_formatting(self):
        a, b = 1, 2
        self.assertEqual("%d + %d = %d" % (a, b, a + b), "1 + 2 = 3")

if __name__ == "__main__":
    unittest.main()
