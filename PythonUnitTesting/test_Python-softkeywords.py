# Feb. 23, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

import unittest
import keyword

import versioncheck

versioncheck.version_check()

print("test_Python-softkeywords.py")


class KeywordsTestCases(unittest.TestCase):
    expected_softkwlist = ["_", "case", "match", "type"]

    def test_softkwlist(self):
        """
        Test that the soft keyword list matches the expected list.
        """
        self.assertEqual(keyword.softkwlist, self.expected_softkwlist)

    def test_issoftkeyword(self):
        """
        Test that the issoftkeyword function returns True for all soft keywords.
        """
        for kwitem in self.expected_softkwlist:
            with self.subTest(kw=kwitem):
                self.assertTrue(keyword.issoftkeyword(kwitem))


if __name__ == "__main__":
    unittest.main()
