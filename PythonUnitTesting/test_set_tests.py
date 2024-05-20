import unittest


class SetTests(unittest.TestCase):
    def test_union(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected_result = {1, 2, 3, 4, 5}
        self.assertEqual(set1.union(set2), expected_result)

    def test_union_operator(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected_result = {1, 2, 3, 4, 5}
        self.assertEqual(set1 | set2, expected_result)

    def test_intersection(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected_result = {3}
        self.assertEqual(set1.intersection(set2), expected_result)

    def test_intersection(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected_result = {3}
        self.assertEqual(set1 & set2, expected_result)


if __name__ == "__main__":
    unittest.main()
