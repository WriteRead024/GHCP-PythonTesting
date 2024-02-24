
# Feb. 24, 2024
# Rich W.
# MSL.l

import unittest

import versioncheck
versioncheck.version_check()

print("test_number-type-conversion.py")

class StringPropertiesTestCases(unittest.TestCase):
    def test_new_properties_on_a_string_raise_error(self):
        """
        string property
        """
        string_var = "string"
        with self.assertRaises(AttributeError):
            string_var.new_property = "new property"
    
    def test_string_is_immutable(self):
        """
        string property
        """
        string_var = "string"
        with self.assertRaises(TypeError):
            string_var[0] = "S"

    def test_substring_start_operation(self):
        """
        Test substring slice start operation.
        """
        string_var = "This is a string."
        substring = string_var[5:]
        self.assertEqual(substring, "is a string.")
    
    def test_substring_start_and_stop_operation(self):
        """
        Test substring slice start and stop operation.
        """
        string_var = "This is a string."
        substring = string_var[5:9]
        self.assertEqual(substring, "is a")

    def test_substring_stop_operation(self):
        """
        Test substring slice stop operation.
        """
        string_var = "This is a string."
        substring = string_var[:4]
        self.assertEqual(substring, "This")

    def test_substring_copy_operation(self):
        """
        Test substring slice copy operation.
        """
        string_var = "This is a string."
        new_string = string_var[:]
        self.assertEqual(new_string, "This is a string.")
        string_var = "This is a different string."
        self.assertNotEqual(new_string, string_var)