
# Feb. 24, 2024
# Rich W.
# with some help from GitHub Copilot
# MSL.l

import sys
import unittest

print("test_number-type-conversion.py")
print("current Python version:", sys.version)
if sys.version_info.major != 3 or sys.version_info.minor != 12:
    raise Warning("This script was written for Python 3.12(.1)")
else:
    print("Python version is the expected 3.12")

class DataAndTypeConversionTestCases(unittest.TestCase):
    def test_type_conversion(self):
        """
        Test type conversion from float to int truncates decimal digit values.
        """
        float_num = 3.14
        int_num = int(float_num)
        self.assertEqual(int_num, 3)

    def test_type_conversion_rounding(self):
        """
        Test round function rounds float to nearest integer and retuns an int.
        """
        float_num = 3.75
        int_num = round(float_num)
        self.assertEqual(int_num, 4)
        self.assertIsInstance(int_num, int)

    def test_type_conversion_error(self):
        """
        Explicit type conversion method from float with decimals to int raises ValueError.
        """
        float_num = "3.14"
        with self.assertRaises(ValueError):
            int_num = int(float_num)

    def test_type_conversion_error_two(self):
        """
        Explicit type conversion method from implicitly typed float with zeroed decimals to int raises ValueError.
        """
        float_num = "3.00"
        with self.assertRaises(ValueError):
            int_num = int(float_num)

    def test_type_conversion_no_error(self):
        """
        Explicit type conversion from explicitly typed float with decimals to does not raise ValueError.
        """
        float_num = float("3.00")
        try:
            int_num = int(float_num)
        except ValueError:
            self.fail("Unexpected ValueError raised")

    def test_type_conversion_no_error_two(self):
        """
        Explicit type conversion from float without decimals to does not raise ValueError.
        """
        float_num = float("3")
        try:
            int_num = int(float_num)
        except ValueError:
            self.fail("Unexpected ValueError raised")
