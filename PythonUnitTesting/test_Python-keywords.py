
# Feb. 23, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

import sys
import unittest
import keyword

print("test_Python-keywords.py")
print("Python version:", sys.version)
if sys.version_info.major != 3 or sys.version_info.minor != 12:
    raise Warning("This script was written for Python 3.12(.1)")
else:
    print("Python version is the expected 3.12")

class KeywordsTestCases(unittest.TestCase):
    expected_kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    def test_kwlist(self):
        """
        Test that the keyword list matches the expected list.
        """
        self.assertEqual(keyword.kwlist, self.expected_kwlist)

    def test_iskeyword(self):
        """
        Test that the iskeyword function returns True for all keywords.
        """
        for kwitem in self.expected_kwlist:
            with self.subTest(kw=kwitem):
                self.assertTrue(keyword.iskeyword(kwitem))

if __name__ == '__main__':
    unittest.main()