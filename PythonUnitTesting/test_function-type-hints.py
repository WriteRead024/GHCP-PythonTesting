# Feb. 24, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

import unittest

import versioncheck

versioncheck.version_check()

print("test_function-type-hints.py")


# The function with type hints that the tests will use.
def concatenate_strings_twice(a: str, b: str) -> str:
    if len(a) == 0:
        return 0
    return str(a) + str(b) + str(a) + str(b)


class KeywordsTestCases(unittest.TestCase):

    def test_concatenate_strings_twice(self):
        """
        Test that the concatenate_strings_twice function returns the expected result.
        """
        self.assertEqual(concatenate_strings_twice("a", "b"), "abab")

    def test_wrong_parameter_type_throws_error(self):
        """
        Test that the concatenate_strings_twice function raises a TypeError if the parameters are not strings.
        """
        try:
            concatenate_strings_twice("1", 2)
        except:
            self.fail("unexpected Error raised")

    def test_wrong_named_parameter_type_throws_error(self):
        """
        Test that the concatenate_strings_twice function does not raises a TypeError.
        """
        try:
            concatenate_strings_twice(a="1", b=2)
        except:
            self.fail("unexpected Error raised")

    def test_empty_string(self):
        """
        concatenate_strings_twice function returns the number 0 if the first parameter is an empty string and does not raise an Error.
        """
        self.assertEqual(concatenate_strings_twice("", "b"), 0)


if __name__ == "__main__":
    ktc = KeywordsTestCases()
    ktc.test_wrong_named_parameter_type_throws_error()
    concatenate_strings_twice("a", 2)
